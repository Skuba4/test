from dotenv import load_dotenv
import os

load_dotenv()  # подгружаем .env из корня или load_dotenv("путь")

DOWNLOAD_PATH = 'downloads'
MAX_FOLDER_SIZE = 1 * 1024 * 1024 * 1024  # 1 ГБ

TOKEN = os.getenv("TOKEN")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
