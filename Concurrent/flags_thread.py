#use threads, which timeslices on a single core (not parallel)
import threading
import time
import requests

class DownloadThread(threading.Thread):
    def __init__(self, img_url, dest_path):
        super().__init__()
        self.img_url = img_url
        self.dest_path = dest_path

    def run(self):
        response = requests.get(self.img_url)
        with open(self.dest_path, 'wb') as f:
            f.write(response.content)
            
def download_all_flags(img_urls, dest_dir):
    threads = []
    for img_url in img_urls:
        img_filename = os.path.basename(img_url)
        dest_path = os.path.join(dest_dir, img_filename)
        thread = DownloadThread(img_url, dest_path)
        thread.start()
        threads.append(thread)
    
    for thread in threads:
        thread.join()
    
def main():
    start_time = time.perf_counter()
    
    img_urls = [
        'https://www.example.com/flags/flag1.jpg',
        'https://www.example.com/flags/flag2.jpg',
        'https://www.example.com/flags/flag3.jpg',
        # Add more flag image URLs here
    ]
    
    dest_dir = 'flags'
    download_all_flags(img_urls, dest_dir)
    
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f'Elapsed time: {elapsed_time:.2f} seconds')

if __name__ == '__main__':
    main()