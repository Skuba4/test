import os
from config import DOWNLOAD_PATH, MAX_FOLDER_SIZE
from services import utils, insta, public
from shared.enums import Platform
import json

EXTENSIONS = [".mp4", ".webm", ".jpg", ".jpeg", ".png", ".webp"]

PLATFORM_MAP = {
    # Platform.INSTAGRAM: insta.download,
    Platform.TIKTOK: public.download,
    Platform.YOUTUBE: public.download,
    Platform.YOUTUBE_SHORT: public.download,
    Platform.VK: public.download,
}

def download_media(link: str) -> str:
    os.makedirs(DOWNLOAD_PATH, exist_ok=True)

    file_hash = utils.hash_link(link)
    target_path = os.path.join(DOWNLOAD_PATH, file_hash)

    # Кэш
    for ext in EXTENSIONS:
        cached = target_path + ext
        if os.path.exists(cached):
            return cached

    utils.cleanup_folder(DOWNLOAD_PATH, MAX_FOLDER_SIZE)

    for domain, handler in PLATFORM_MAP.items():
        if domain in link:
            return handler(link, target_path)

    raise Exception("Неподдерживаемая платформа")

def get_media_info(link: str) -> dict:
    file_hash = utils.hash_link(link)
    info_path = os.path.join(DOWNLOAD_PATH, file_hash + ".json")

    # 📦 Читаем из кэша, если уже есть
    if os.path.exists(info_path):
        with open(info_path, "r", encoding="utf-8") as f:
            return json.load(f)

    # 🆕 Иначе получаем свежую инфу
    for domain, handler in PLATFORM_MAP.items():
        if domain in link:
            if domain == Platform.INSTAGRAM:
                info = insta.extract_info(link)
            else:
                info = public.extract_info(link)

            # 💾 Сохраняем инфу в JSON рядом с видео
            with open(info_path, "w", encoding="utf-8") as f:
                json.dump(info, f, ensure_ascii=False)

            return info

    return {
        "platform": "Неизвестно",
        "username": None,
        "caption": ""
    }
