from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Start, Cancel
from aiogram_dialog.widgets.text import Multi, Const

from src.tgbot.dialogs.states import MainMenu, CompanySelection


main_menu_dialog = Dialog(
    Window(
        Multi(
            Const("Welcome to the Financial Data Bot!"),
            Const("Please select an option to continue:"),
            sep="\n\n",
        ),
        Start(
            Const("Select a company to get its financial data"),
            id="company_financial_data",
            state=CompanySelection.spreadsheet_selection,
        ),
        Cancel(
            Const("❌ Exit"),
        ),
        state=MainMenu.main,
    ),
)
