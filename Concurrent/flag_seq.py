#download flags sequentially, no currency
import requests
import os
import time

def download_flag(img_url, dest_path):
    response = requests.get(img_url)
    with open(dest_path, 'wb') as f:
        f.write(response.content)

def download_all_flags(img_urls, dest_dir):
    os.makedirs(dest_dir, exist_ok=True)
    for img_url in img_urls:
        img_filename = os.path.basename(img_url)
        dest_path = os.path.join(dest_dir, img_filename)
        download_flag(img_url, dest_path)

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
