from aiogram import Bot, Dispatcher
import logging
import sys
import asyncio
from aiogram.enums import ParseMode

from config import TOKEN
from handlers.cmd_handlers import cmd_router
from handlers.msg_handlers import msg_router


async def main():
    bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
    db = Dispatcher()
    db.include_routers(cmd_router,msg_router)
    await db.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("Bot stopped")
