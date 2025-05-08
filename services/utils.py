import os
import hashlib
import requests

def hash_link(link: str) -> str:
    return hashlib.sha256(link.encode()).hexdigest()

def cleanup_folder(folder_path: str, max_size: int):
    total_size = 0
    files = []

    for root, _, filenames in os.walk(folder_path):
        for f in filenames:
            path = os.path.join(root, f)
            if os.path.isfile(path):
                size = os.path.getsize(path)
                total_size += size
                files.append((path, size))

    if total_size <= max_size:
        return

    files.sort(key=lambda x: os.path.getctime(x[0]))

    while total_size > max_size and files:
        path, size = files.pop(0)
        os.remove(path)
        total_size -= size

def try_download_image(url: str, output_path: str) -> str:
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open(output_path, "wb") as f:
            for chunk in r.iter_content(1024):
                f.write(chunk)
        return output_path
    raise Exception("Не удалось скачать изображение")
