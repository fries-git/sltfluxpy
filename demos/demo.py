from sltfluxpy import *
import os
from dotenv import load_dotenv
import time

load_dotenv()
token = os.getenv("FLUXTOKEN")
email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

print(login(email, password))