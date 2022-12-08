from os import environ

from aiogram import Bot, Dispatcher

from bot.game import Game
from bot.handlers import router


async def run():
    bot_token = environ.get("TOKEN")

    bot = Bot(token=bot_token)
    dp = Dispatcher()
    dp.include_router(router)

    game = Game()
    kwargs = {
        "game": game,
    }

    await dp.start_polling(
        bot,
        allowed_updates=dp.resolve_used_update_types(),
        **kwargs,
    )
