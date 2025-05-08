from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

router = Router()


class Status(StatesGroup):
    st = State()


@router.message(Command("start"))
async def start_handler(message: Message, state: FSMContext):
    await state.set_state(Status.st)
    print(message.text)
    await message.answer(f"Instagram, TikTok, YouTube и VK")


@router.message(Command("stop"))
async def stop_handler(message: Message, state: FSMContext):
    print(message.text)
    if await state.get_state():
        await state.clear()
        await message.answer(f"THE END")
