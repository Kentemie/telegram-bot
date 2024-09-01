import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from aiogram_dialog import setup_dialogs

from src.utils import setup_logging

from src.core.config import settings

from src.tgbot.dialogs import main_menu_dialog, company_selection_dialog
from src.tgbot.handlers import routers_list
from src.tgbot.managers.process_pool import process_pool_manager


async def main():
    setup_logging()

    bot = Bot(
        token=settings.TELEGRAM_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    dp = Dispatcher()

    dp.include_routers(*routers_list)
    dp.include_routers(main_menu_dialog, company_selection_dialog)

    setup_dialogs(dp)

    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        process_pool_manager.shutdown()
        logging.error("The bot has been turned off!")
