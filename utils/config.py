import os
from dotenv import load_dotenv

load_dotenv()  # load .env if present

class Config:
    BASE_URL = os.getenv("BASE_URL", "https://the-internet.herokuapp.com")
    USERNAME = os.getenv("USERNAME", "tomsmith")
    PASSWORD = os.getenv("PASSWORD", "SuperSecretPassword!")
    BROWSER = os.getenv("BROWSER", "chrome")  # chrome/firefox/edge
