from pathlib import Path  # python3 only
import os

from pipenv.vendor.dotenv import load_dotenv


env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

secret = os.getenv('PASSWORD')

print(secret)
