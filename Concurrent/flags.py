# This project is not part of the Dessert Shop system. In this project, you will download jpegs for flags from all the countries in the world from a public website. The files appear in the following web folder:
# The names of the files have the following form <country_name>.jpg. For example, the jpeg for the United States is United_States.jpg. The country names are in the input file flags.txt, which is provided for you.

# Write three similar programs that do the following:
# Download all flag files into a “flags” subdirectory
# Report the total number of bytes downloaded
# Report the elapsed execution time of the script using time.perf_counter()

# Write a program that downloads all the flag files into a “flags” subdirectory. If the “flags” subdirectory does not exist, the program should create it. If the “flags” subdirectory exists, the program should delete all the files in it before downloading the new flags. Report the total number of bytes downloaded and the elapsed execution time of the script using time.perf_counter().

# The three versions of the program must be:
# flags_seq.py: download flags sequentially, no concurrency
# flags_thread.py: use threads, which timeslices on a single core
# flags_smp.py: use multiprocessing for multicore parallelism

# Use the requests module discussed in class to make the HTTP requests.
# Inspect your flags directory after each execution to verify that all the jpegs have been freshly downloaded.
# The three corresponding output files must be:
# flags_seq.out
# flags_thread.out
# flags_smp.out
import os
import time
import sys
import requests


COUNTRY_NAMES = "flags.txt"
BASE_URL = 'http://flupy.org/data/flags'

def get_country_names():
    with open(COUNTRY_NAMES) as f:
        return f.read().splitlines()
    
def download_flag(country, base_url):
    url = '{}/{cc}/{cc}.gif'.format(base_url, cc=country.lower())
    resp = requests.get(url)
    return resp.content

def save_flag(img, filename):
    path = os.path.join('flags', filename)
    with open(path, 'wb') as fp:
        fp.write(img)

def download_many(cc_list):
    # save flags as jpegs
    for cc in cc_list:
        image = download_flag(cc, BASE_URL)
        show(cc)
        save_flag(image, cc.lower() + '.jpg')
    return len(cc_list)
        
def show(text):
    print(text, end=' ')
    sys.stdout.flush()

def main(download_many):
    #Report the total number of bytes downloaded
    total_bytes = 0
    for country in get_country_names():
        total_bytes += len(download_flag(country, BASE_URL))
    t0 = time.perf_counter()
    count = download_many(get_country_names())
    elapsed = time.perf_counter() - t0
    msg = '{} flags downloaded in {:.2f}s'
    print(msg.format(count, elapsed))
    print('Total bytes downloaded: ' + str(total_bytes))

if __name__ == '__main__':
    main(download_many)