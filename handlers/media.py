from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, FSInputFile

from services.common import download_media, get_media_info

router = Router()


@router.message(lambda msg: "https://" in msg.text)
async def link_handler(message: Message, state: FSMContext):
    print(message.text)
    if await state.get_state():
        link = message.text.strip()

        if not any(x in link for x in ["instagram.com", "tiktok.com", "youtube.com", "youtu.be", "vk.com"]):
            await message.answer("Только Instagram, TikTok, YouTube и VK")
            return

        dm = await message.answer("⏳ Скачиваю...")

        try:
            file_path = download_media(link)
            media_info = get_media_info(link)  # 👈 добавим получение инфы о видео (соцсеть, username, caption)

            media = FSInputFile(file_path)
            ext = file_path.lower()

            if ext.endswith((".jpg", ".jpeg", ".png", ".webp")):
                await message.answer_photo(photo=media)
            elif ext.endswith((".mp4", ".webm", ".mkv")):
                await message.answer_video(video=media, supports_streaming=True)
            else:
                await message.answer("⚠️ Файл скачан, но его нельзя отправить через Telegram.")
                return

            # Формируем текст
            platform = media_info.get("platform", "Неизвестно")
            username = media_info.get("username", None)
            caption = media_info.get("caption", "")

            emoji_map = {
                "Instagram": "📸",
                "YouTube": "🔴",
                "TikTok": "🎵",
                "VK": "▶️"
            }

            header = f"*{emoji_map.get(platform, '')} {platform}*"
            blocks = []

            if platform == "Instagram" and username:
                blocks.append(f"👤: `{username}`")

            if caption:
                blocks.append(f"💬: `{caption}`")

            formatted_message = header + "\n\n" + "\n\n".join(blocks) if blocks else header

            await message.answer(formatted_message, parse_mode="Markdown")
            await dm.delete()

        except Exception as e:
            await message.answer(f"Ошибка при загрузке: {e}")


@router.message(F.text)
async def other_handler(message: Message, state: FSMContext):
    if await state.get_state():
        await message.answer("Instagram, TikTok, YouTube и VK")