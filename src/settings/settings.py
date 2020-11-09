from dotenv import load_dotenv
from pathlib import Path


def load_env():
    load_dotenv(dotenv_path=f'{Path(__file__).parent}/.env')
