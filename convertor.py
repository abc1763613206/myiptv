import csv
import os

def csv_to_m3u8(input_csv, output_m3u8, encoding='utf-8'):
    """
    Convert CSV file to M3U8 format
    
    Args:
        input_csv (str): Path to input CSV file
        output_m3u8 (str): Path to output M3U8 file
    """
    try:
        with open(input_csv, 'r', encoding=encoding) as csv_file, \
             open(output_m3u8, 'w', encoding='utf-8') as m3u8_file:
            
            # Write M3U8 header
            m3u8_file.write('#EXTM3U\n')
            
            # Read CSV file
            csv_reader = csv.DictReader(csv_file)
            
            # Convert each row to M3U8 format
            for row in csv_reader:
                channel = row['Channel']
                group = row['Group']
                source = row['Source']
                link = row['Link']
                
                # Write channel information
                m3u8_file.write(f'#EXTINF:-1 group-title="{group}" tvg-name="{channel}" tvg-logo="" tv-source="{source}",{channel}\n')
                m3u8_file.write(f'{link}\n')
                
        return True
    
    except Exception as e:
        print(f"Error converting CSV to M3U8: {str(e)}")
        return False

def m3u8_to_csv(input_m3u8, output_csv, encoding='utf-8'):
    """
    Convert M3U8 file to CSV format
    
    Args:
        input_m3u8 (str): Path to input M3U8 file
        output_csv (str): Path to output CSV file
    """
    try:
        with open(input_m3u8, 'r', encoding=encoding) as m3u8_file, \
             open(output_csv, 'w', encoding=encoding, newline='') as csv_file:
            
            writer = csv.DictWriter(csv_file, fieldnames=['Channel', 'Group', 'Source', 'Link'])
            writer.writeheader()
            
            lines = m3u8_file.readlines()
            i = 0
            while i < len(lines):
                line = lines[i].strip()
                if line.startswith('#EXTINF:'):
                    info = line.split('"')
                    group = info[1] if len(info) > 1 else ''
                    channel = info[3] if len(info) > 3 else ''
                    source = info[7] if len(info) > 7 else ''
                    name = info[-1].split(',')[-1]
                    
                    if i + 1 < len(lines):
                        link = lines[i + 1].strip()
                        writer.writerow({
                            'Channel': name,
                            'Group': group,
                            'Source': source,
                            'Link': link
                        })
                i += 1
                
        return True
        
    except Exception as e:
        print(f"Error converting M3U8 to CSV: {str(e)}")
        return False

def tvlist_to_m3u8(input_file, output_file, encoding='utf-8'):
    """
    Convert TVList file to M3U8 format
    
    Args:
        input_file (str): Path to input TVList file
        output_file (str): Path to output M3U8 file
    """
    try:
        with open(input_file, 'r', encoding=encoding) as tvlist_file, \
             open(output_file, 'w', encoding='utf-8') as m3u8_file:
            
            # Write M3U8 header
            m3u8_file.write('#EXTM3U\n')
            
            for line in tvlist_file:
                parts = line.strip().split(',')
                Channel = parts[0]
                Link = parts[1]
                m3u8_file.write(f'#EXTINF:-1 tvg-name="{Channel}",{Channel}\n')
                m3u8_file.write(f'{Link}\n') 
        return True
    except Exception as e:
        print(f"Error converting TVList to M3U8: {str(e)}")
        return False

def tvgroup_to_m3u8(output_file):
    MAPPING = {
        "cctv": "央视频道",
        "weishi": "卫视频道",
        "difang": "地方频道",
        "special": "特色频道"
    }
    DIR = os.path.join(os.path.dirname(__file__), 'groups')
    try:
        with open(output_file, 'w', encoding='utf-8') as m3u8_file:
            m3u8_file.write('#EXTM3U\n')
            for group in MAPPING:
                file = os.path.join(DIR, f"{group}.txt")
                if os.path.exists(file):
                    with open(file, 'r', encoding='gb18030') as f:
                        for line in f:
                            parts = line.strip().split(',')
                            Channel = parts[0]
                            Link = parts[1]
                            m3u8_file.write(f'#EXTINF:-1 group-title="{MAPPING[group]}" tvg-name="{Channel}",{Channel}\n')
                            m3u8_file.write(f'{Link}\n')
        return True
    except Exception as e:
        print(f"Error converting TVGroup to M3U8: {str(e)}")
        return False

if __name__ == "__main__":
    input_file = "data.csv"
    output_file = "playlist.m3u8"
    
    # csv_to_m3u8(input_file, output_file, encoding='gb18030')
    tvgroup_to_m3u8(output_file)