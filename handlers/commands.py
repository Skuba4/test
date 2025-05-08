from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from database.engine import async_session
from database.models import Users

router = Router()


class Status(StatesGroup):
    st = State()


@router.message(Command("start"))
async def start_handler(message: Message, state: FSMContext):
    telegram_id = message.from_user.id
    username = message.from_user.username or "без username"

    async with async_session() as session:
        existing_user = await session.get(Users, telegram_id)
        if not existing_user:
            new_user = Users(id=telegram_id, username=username)
            session.add(new_user)
            await session.commit()
            await message.answer("✅ Пользователь сохранён.")
        else:
            await message.answer("👋 Вы уже есть в базе данных.")

    await state.set_state(Status.st)
    print(message.text)
    await message.answer(f"Кидай ссылку Instagram, TikTok, YouTube и VK")


@router.message(Command("stop"))
async def stop_handler(message: Message, state: FSMContext):
    print(message.text)
    if await state.get_state():
        await state.clear()
        await message.answer(f"THE END")
