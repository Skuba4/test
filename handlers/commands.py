from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram import F

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

router = Router()


class Status(StatesGroup):
    st = State()


@router.message(Command("start"))
async def start_handler(message: Message, state: FSMContext):
    await state.set_state(Status.st)
    await message.answer(f"Начинаю работать")


@router.message(F.text.lower().contains('олег пидор'))
async def pidor_handler(message: Message, state: FSMContext):
    user_id = message.from_user.id
    username = message.from_user.username or "без username"

    if await state.get_state():
        await message.answer(user_id, username)


@router.message(Command("stop"))
async def stop_handler(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(f"THE END")


@router.message(F.text)
async def text_handler(message: Message, state: FSMContext):
    if await state.get_state():
        await message.answer("Обычное сообщение")
