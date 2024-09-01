# Telegram Bot

Этот Telegram бот позволяет отображать финансовые данные из Google Sheets. Чтобы запустить бота, выполните следующие шаги.

## Установка

### 1. Получение токена Telegram бота

1. Откройте Telegram и найдите пользователя `@BotFather`.
2. Отправьте команду `/newbot` и следуйте инструкциям для создания нового бота.
3. Скопируйте полученный токен API.

### 2. Создание проекта в Google Cloud

1. Перейдите на [Google Cloud Console](https://console.cloud.google.com/).
2. Создайте новый проект или выберите существующий.
3. В меню "API & Services" выберите "Credentials".
4. Создайте новый **Service Account**:
   - Укажите имя и описание.
   - Выберите роль `Editor` для доступа к редактированию Google Sheets и Google Drive.
   - Нажмите "Done".
5. В разделе "Keys" создайте новый ключ в формате JSON.
6. Скачайте ключ и поместите его в директорию `certs` в корне проекта под именем `service_account.json`.

### 3. Предоставление доступа к Google Sheets и Google Drive

1. Откройте Google Drive и выберите нужные таблицы.
2. Предоставьте доступ вашему сервисному аккаунту:
   - Нажмите "Share" на таблице.
   - Введите email вашего сервисного аккаунта (выглядит как `name@project-id.iam.gserviceaccount.com`).
   - Выберите права доступа (чтение, редактирование и т.д.).

### 4. Настройка `.env` файла

1. В корне проекта создайте файл `.env`.
2. Сохраните следующие переменные окружения:

```plaintext
TELEGRAM_BOT_TOKEN=<Ваш_токен_от_BotFather>

GOOGLE_SERVICE__KEY_PATH=certs/service_account.json
GOOGLE_SERVICE__SHEETS__SCOPES=https://www.googleapis.com/auth/spreadsheets
GOOGLE_SERVICE__DRIVE__SCOPES=https://www.googleapis.com/auth/drive
```