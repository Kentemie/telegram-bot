from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from aiogram_dialog import DialogManager, StartMode

from src.tgbot.dialogs.states import MainMenu


start_router = Router()


@start_router.message(CommandStart())
async def start_handler(message: Message, dialog_manager: DialogManager):  # noqa
    await dialog_manager.start(MainMenu.main, mode=StartMode.RESET_STACK)
