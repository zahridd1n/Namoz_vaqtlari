import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

from nomoz_vati import namoz_time as myfunc

# Bot token can be obtained via https://t.me/BotFather
TOKEN = "6898013821:AAEuXoyfnW1YQw3sVVbc566-1iUMkE3BSj4"

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    # Most event objects have aliases for API methods that can be called in events' context
    # For example if you want to answer to incoming message you can use `message.answer(...)` alias
    # and the target chat will be passed to :ref:`aiogram.methods.send_message.SendMessage`
    # method automatically or call API method directly via
    # Bot instance: `bot.send_message(chat_id=message.chat.id, ...)`
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")


@dp.message()
async def echo_handler(message: Message) -> None:
    """
    Handler will forward receive a message back to the sender

    By default, message handler will handle all message types (like a text, photo, sticker etc.)
    """
    try:
        if message.text == 'Fergana' or message.text == 'Farg’ona' or message.text == "Far'gona":
            txt = myfunc("Farg'ona")
        else:
            txt = myfunc(message.text)
        if txt:
            # Send a copy of the received message
            await message.answer(
                f"Kun: {txt['date']} \nHudud: {txt['region']} \nHafta kuni: {txt['weekday']} \n {html.bold('Namoz Vaqtlari')}\n {txt["times"]}\n")
        else:

            # But not all the types is supported to be copied so need to handle it
            await message.answer("Bunday malumot topilmadi")
    except:
        await message.answer(f"Shahar nomini xato kiritngiz")

async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
