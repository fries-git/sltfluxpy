from sltfluxpy import *
from dotenv import load_dotenv
import os

load_dotenv()

settoken(login(os.getenv("EMAIL"),os.getenv("PASSWORD")))