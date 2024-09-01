from aiogram.fsm.state import StatesGroup, State


class MainMenu(StatesGroup):
    main = State()


class CompanySelection(StatesGroup):
    spreadsheet_selection = State()
    company_selection = State()
    metric_type_selection = State()
    chart_selection = State()
