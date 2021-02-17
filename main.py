import csv
import sys
import json
import os
import re
import traceback
import requests
import subprocess
import time
import shutil
from ffmpy import FFprobe
from subprocess import PIPE
from sys import stdout
from termcolor import colored, RESET
from datetime import datetime
from func_timeout import func_set_timeout, FunctionTimedOut
dt=datetime.now()
# Channel	Group	Source	Link

SKIP_FFPROBE_MESSAGES = [re.compile(pattern) for pattern in (
	'Last message repeated',
	'mmco: unref short failure',
	'number of reference frames .+ exceeds max',
)]

uniqueList = []

@func_set_timeout(12)
def get_stream(num, clist, uri):
    try:
        ffprobe = FFprobe(inputs={uri: '-v error -show_format -show_streams -print_format json'})
        cdata = json.loads(ffprobe.run(stdout=PIPE,stderr=PIPE)[0].decode('utf-8'))
        return cdata
    except Exception as e:
        #traceback.print_exc()
        print('[{}] {}({}) Error:{}'.format(str(num), clist[0], clist[2], str(e)))
        return False

def check_channel(clist,num):
    # clist 为一行 csv
    uri = clist[3]
    try:
        r = requests.get(clist[3], timeout=2) # 先测能不能正常访问
        if(r.status_code == requests.codes.ok):
            #ffprobe = FFprobe(inputs={uri: '-v warning'})
            #errors = tuple(filter(
			#    lambda line: not (line in ('', RESET) or any(regex.search(line) for regex in SKIP_FFPROBE_MESSAGES)),
			#    ffprobe.run(stderr=PIPE)[1].decode('utf-8').split('\n')
		    #))
            #if errors: # https://github.com/Jamim/iptv-checker/blob/master/iptv-checker.py#L26
            #    print('[{}] {}({}) Error:{}'.format(str(num), clist[0], clist[2], str(errors)))
            #    return False
            #else: # 查视频信息
            cdata = get_stream(num, clist, uri)
            if cdata:
                flagAudio = 0
                flagVideo = 0
                vwidth = 0
                vheight = 0
                for i in cdata['streams']:
                    if i['codec_type'] == 'video':
                        flagVideo = 1
                        if vwidth <= i['coded_width']: # 取最高分辨率
                            vwidth = i['coded_width']
                            vheight = i['coded_height']
                    elif i['codec_type'] == 'audio':
                        flagAudio = 1
                if flagAudio == 0:
                    print('[{}] {}({}) Error: Video Only!'.format(str(num), clist[0], clist[2]))
                    return False
                if flagVideo == 0:
                    print('[{}] {}({}) Error: Audio Only!'.format(str(num), clist[0], clist[2]))
                    return False
                print('[{}] {}({}) PASS: {}*{}'.format(str(num), clist[0], clist[2], vwidth, vheight))
                return [vwidth,vheight]
            else:
                return False
        else:
            print('[{}] {}({}) Error:{}'.format(str(num), clist[0], clist[2], str(r.status_code)))
            return False
    except Exception as e:
        #traceback.print_exc()
        print('[{}] {}({}) Error:{}'.format(str(num), clist[0], clist[2], str(e)))
        return False

def print_info():
    print('Time: {}-{}-{} {}:{}'.format(dt.year,dt.month,dt.day,dt.hour,dt.minute))
    #subprocess.run(['ffprobe'])

def rm_files(target, selection):
    if selection == 1:  # 删目录
        try:
            shutil.rmtree(target)
        except OSError:
            pass
        try:
            os.mkdir(target)
        except OSError:
            pass
    else: # 删文件
        try:
            os.remove(target)
        except OSError:
            pass   
        

def main():
    print_info()
    Total = 0
    fulltimes = '-{}{}{}{}{}'.format(dt.year,dt.month,dt.day,dt.hour,dt.minute) # 时间后缀
    # times = fulltimes # 有时间后缀
    times = '' # 无时间后缀
    # 清空旧文件
    rm_files('groups',1)
    rm_files('merged.txt',2)
    rm_files('merged-simple.txt',2)
    with open('data.csv') as f:
        f_csv = csv.reader(f)
        headers = next(f_csv)
        num = 1
        with open('data{}.csv'.format(fulltimes), 'a+') as f0: # 写入检测后新data
            print('Channel,Group,Source,Link', file=f0)
            for row in f_csv:
                try:
                    if row[3] in uniqueList:
                        ret = False
                    else:
                        uniqueList.append(row[3]) 
                        ret = check_channel(row,num)
                except FunctionTimedOut as e:
                    #traceback.print_exc()

                    print('[{}] {}({}) Error:{}'.format(str(num), row[0], row[2], str(e)))
                    ret = False
                if(ret): # 通过，写入
                    with open('groups/{}{}.txt'.format(row[1],times), 'a+') as f1:
                        print('{}({}-{}*{}),{}'.format(row[0],row[2],ret[0],ret[1],row[3]), file=f1)
                    with open('groups/{}-simple{}.txt'.format(row[1],times), 'a+') as f1:
                        print('{},{}'.format(row[0],row[3]), file=f1)
                    with open('merged{}.txt'.format(times),'a+') as f1:
                        print('{}({}-{}*{}),{}'.format(row[0],row[2],ret[0],ret[1],row[3]), file=f1)
                    with open('merged-simple{}.txt'.format(times),'a+') as f1:
                        print('{},{}'.format(row[0],row[3]), file=f1)
                    print('{},{},{},{}'.format(row[0],row[1],row[2],row[3]), file=f0)
                    Total = Total + 1
                num = num + 1
                time.sleep(0.3)
    print('Total: {}'.format(Total))
if __name__ == '__main__':
    main()



