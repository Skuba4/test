from dotenv import load_dotenv
import os

load_dotenv()  # подгружаем .env из корня или load_dotenv("путь")

DOWNLOAD_PATH = 'downloads'
MAX_FOLDER_SIZE = 1 * 1024 * 1024 * 1024  # 1 ГБ
TOKEN = os.getenv("TOKEN")
