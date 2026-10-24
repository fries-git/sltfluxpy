from sltfluxpy import *
import os
from dotenv import load_dotenv
import time

load_dotenv()
token = os.getenv("FLUXTOKEN")

id = sendmessage(token, 1485743778301133291, "Stardance Demo!")["id"]
time.sleep(5)
editmessage(token, 1485743778301133291, id, "Stardance Demo but I edited the message!")