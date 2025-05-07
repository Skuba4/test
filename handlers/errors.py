from aiogram.dispatcher.middlewares.base import BaseMiddleware
from aiogram.types import Update


class ErrorMiddleware(BaseMiddleware):
    async def __call__(self, handler, event: Update, data: dict):
        try:
            return await handler(event, data)
        except Exception as e:
            print(f"[ERROR] {type(e).__name__}: {e}")
