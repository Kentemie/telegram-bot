from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from colorama import Back


async def close_dialog(
    callback_query: CallbackQuery,  # noqa
    widget: Back,  # noqa
    dialog_manager: DialogManager,
    **kwargs  # noqa
):
    await dialog_manager.done()
