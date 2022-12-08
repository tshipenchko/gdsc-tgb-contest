from aiogram import Router, F, types
from aiogram.filters import CommandStart, Command
from aiogram.methods import SendMessage

from bot.game import Game

router = Router()


@router.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.reply(
        "Welcome to the guess the number game\n"
        "Please read the rules:\n"
        "1. I will generate a number from 1 to 100\n"
        "2. You need to guess it\n"
        "3. If your number is bigger than mine, I will tell you 'Too big'\n"
        "4. If your number is smaller than mine, I will tell you 'Too small'\n"
        "5. If you guess the number, you will get 1 point\n"
        "6. You can get the top 10 players by using /top command\n"
        "7. You can get your score by using /score command\n"
        "8. The game is multiplayer and online. Number will change after each guess\n"
    )


@router.message(Command("score"))
async def cmd_score(message: types.Message, game: Game):
    score = game.get_score(message.from_user.id)
    await message.reply(f"Your score is {score}")


@router.message(Command("top"))
async def cmd_top(message: types.Message, game: Game):
    top = game.get_top()
    text = "\n".join(
        f"{i + 1}. {'You' if user_id == message.from_user.id else user_id}: {score}"
        for i, (user_id, score) in enumerate(top)
    )
    await message.reply(text)


@router.message(F.text.isdigit())
async def guess_number(message: types.Message, game: Game):
    number = int(message.text)
    await message.reply(game.check_number(message.from_user.id, number))


@router.message()
async def unknown(message: types.Message):
    return SendMessage(
        chat_id=message.chat.id,
        text="Bro, what are you doing? I understand only commands and digits",
        reply_to_message_id=message.message_id,
    )


@router.message(F.text)
async def not_a_digit(message: types.Message):
    await message.reply("Please, enter a digit")
