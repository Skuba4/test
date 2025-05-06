from dotenv import load_dotenv
import os

load_dotenv()           # подгружаем .env из корня или load_dotenv("путь")

TOKEN = os.getenv("TOKEN")


