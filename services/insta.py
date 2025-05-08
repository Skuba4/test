# import os
# import requests
# from instagrapi import Client
# from config import INSTA_USER, INSTA_PASS, USE_INSTA_SESSION
#
# _session_path = f"session_{INSTA_USER}.json"
# _cl = None  # клиент создаётся один раз
#
# def download(link: str, target_path: str) -> str:
#     global _cl
#     if _cl is None:
#         _cl = _auth()
#
#     if "/stories/" in link:
#         try:
#             # Пытаемся вытащить конкретную сториз
#             story_pk = _cl.story_pk_from_url(link)
#             return _download_single_story(story_pk, target_path)
#         except Exception:
#             # fallback на загрузку всей пачки сторис
#             return _download_story_batch(link, target_path)
#
#     if _is_profile_link(link):
#         return _download_avatar(link, target_path)
#
#     media_pk = _cl.media_pk_from_url(link)
#     media = _cl.media_info(media_pk)
#
#     # Карусель
#     if hasattr(media, "resources") and media.resources:
#         res = media.resources[0]
#         url = res.video_url or res.thumbnail_url or res.display_url
#         ext = ".mp4" if res.video_url else ".jpg"
#         return _save_url(url, target_path + ext)
#
#     # Фото или видео
#     url = media.video_url or media.thumbnail_url or media.display_url
#     ext = ".mp4" if media.media_type == 2 else ".jpg"
#     return _save_url(url, target_path + ext)
#
#
# def _auth() -> Client:
#     cl = Client()
#     if USE_INSTA_SESSION and os.path.exists(_session_path):
#         cl.load_settings(_session_path)
#         cl.login(INSTA_USER, INSTA_PASS)
#     else:
#         cl.login(INSTA_USER, INSTA_PASS)
#         if USE_INSTA_SESSION:
#             cl.dump_settings(_session_path)
#     return cl
#
#
# def _download_single_story(story_pk: int, target_path: str) -> str:
#     media = _cl.story_info(story_pk)
#     url = media.video_url or media.thumbnail_url or media.display_url
#     if not url:
#         raise Exception("Сториз не найдена или недоступна")
#     ext = ".mp4" if media.video_url else ".jpg"
#     return _save_url(url, target_path + ext)
#
#
# def _download_story_batch(link: str, target_path: str) -> str:
#     username = _extract_username(link)
#     user_id = _cl.user_id_from_username(username)
#     stories = _cl.user_stories(user_id)
#     for story in stories:
#         url = story.video_url or story.thumbnail_url or story.display_url
#         ext = ".mp4" if story.video_url else ".jpg"
#         return _save_url(url, target_path + ext)
#     raise Exception("Нет активных сторис")
#
#
# def _download_avatar(link: str, target_path: str) -> str:
#     username = _extract_username(link)
#     info = _cl.user_info_by_username(username)
#     return _save_url(info.profile_pic_url_hd, target_path + ".jpg")
#
#
# def _save_url(url: str, output_path: str) -> str:
#     r = requests.get(url, stream=True)
#     if r.status_code == 200:
#         with open(output_path, "wb") as f:
#             for chunk in r.iter_content(1024):
#                 f.write(chunk)
#         return output_path
#     raise Exception(f"Не удалось скачать файл: {url}")
#
#
# def _extract_username(link: str) -> str:
#     parts = link.rstrip("/").split("/")
#     if "stories" in parts:
#         idx = parts.index("stories")
#         return parts[idx + 1]
#     if len(parts) >= 4 and parts[3] != "":
#         return parts[3]
#     raise Exception("Не удалось извлечь username из ссылки")
#
#
# def _is_profile_link(link: str) -> bool:
#     parts = link.rstrip("/").split("/")
#     return len(parts) == 4 and "instagram.com" in parts[2]
#
# def extract_info(link: str) -> dict:
#     global _cl
#     if _cl is None:
#         _cl = _auth()
#
#     try:
#         # stories или обычный пост
#         if "/stories/" in link:
#             story_pk = _cl.story_pk_from_url(link)
#             media = _cl.story_info(story_pk)
#         else:
#             media_pk = _cl.media_pk_from_url(link)
#             media = _cl.media_info(media_pk)
#
#         username = f"@{media.user.username}" if hasattr(media, "user") and media.user.username else "Неизвестно"
#         caption = media.caption_text or ""
#     except Exception:
#         username = "Неизвестно"
#         caption = ""
#
#     return {
#         "platform": "Instagram",
#         "username": username,
#         "caption": caption.strip()
#     }
