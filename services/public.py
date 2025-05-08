from yt_dlp import YoutubeDL
import os


def download(link: str, target_path: str) -> str:
    ydl_opts = {
        "outtmpl": f"{target_path}.%(ext)s",
        "format": "best[ext=mp4][vcodec^=avc1]/best[ext=mp4]/best",
        "quiet": True,
        "noplaylist": True,
    }

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(link, download=True)
        filename = ydl.prepare_filename(info)

    return _find_downloaded_file(filename)


def _find_downloaded_file(base: str) -> str:
    for ext in [".mp4", ".webm", ".jpg", ".jpeg", ".png", ".webp"]:
        if os.path.exists(base + ext):
            return base + ext
        if os.path.exists(base):
            return base
    raise Exception("Файл не найден после загрузки")


def extract_info(link: str) -> dict:
    ydl_opts = {
        "quiet": True,
        "skip_download": True,
    }

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(link, download=False)

    caption = info.get("description") or info.get("title") or ""

    platform = "Unknown"
    if "youtube.com" in link or "youtu.be" in link:
        platform = "YouTube"
    elif "tiktok.com" in link:
        platform = "TikTok"
    elif "vk.com" in link:
        platform = "VK"

    return {
        "platform": platform,
        "username": "",
        "caption": caption.strip()
    }
