import os
import requests
import gzip
import io
import time
from bs4 import BeautifulSoup

url = "http://epg.51zmt.top:8000/api/upload/"


def get_epg(a, b):
    f = os.path.join(a, b)
    if ("utf8" in f) or ("ignored" in f):
        return
    files = {"myfile": open(f, "rb")}
    print("Converting {}".format(f))
    r = requests.post(url, files=files)
    print(r.text)
    soup = BeautifulSoup(r.text, "html.parser")
    links = soup.find_all("a")
    for item in links:
        m3u8url = item.get("href")
        print(m3u8url)
        r1 = requests.get(m3u8url)
        name = str(b)[:-4] + ".m3u"
        with open(name, "wb") as f1:
            f1.write(r1.content)
    return


if __name__ == "__main__":
    for root, dirs, files in os.walk("..", topdown=False):
        for name in files:
            if ".txt" in name:
                # print(os.path.join(root, name))
                get_epg(root, name)
