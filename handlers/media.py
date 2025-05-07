import asyncio

from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

router = Router()


@router.message(lambda msg: "https://" in msg.text)
async def handle_link(message: Message, state: FSMContext):
    print(message.text)
    if await state.get_state():
        msg = await message.answer("⏳ Скачиваю...")
        await asyncio.sleep(2)
        await message.answer("ВИДЕО")
        await asyncio.sleep(1)
        await message.answer("ТЕКСТ")
        await msg.delete()  # удаляем сообщение "


@router.message(F.text.lower().contains('1'))
async def pidor_handler(message: Message, state: FSMContext):
    print(message.text)
    if await state.get_state():
        await message.answer(f"тест")


@router.message(F.text)
async def text_handler(message: Message, state: FSMContext):
    print(message.text)
    if await state.get_state():
        await message.answer("Обычное сообщение")
