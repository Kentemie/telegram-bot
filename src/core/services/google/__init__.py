from src.core.config import settings

from .drive import GoogleDriveManager
from .sheets import GoogleSheetsManager


google_drive_manager = GoogleDriveManager(
    service_account_key_path=settings.GOOGLE_SERVICE.KEY_PATH,
    scopes=settings.GOOGLE_SERVICE.DRIVE.SCOPES,
)


google_sheets_manager = GoogleSheetsManager(
    service_account_key_path=settings.GOOGLE_SERVICE.KEY_PATH,
    scopes=settings.GOOGLE_SERVICE.SHEETS.SCOPES,
    drive_manager=google_drive_manager,
)
