from sltfluxpy import *
import os
from dotenv import load_dotenv
import time

load_dotenv()
email, password = os.getenv("EMAIL"), os.getenv("PASSWORD")
token = login(email, password)["token"]

id = sendmessage(token, 1485743778301133291, "Stardance Demo!")["id"]
time.sleep(3)
editmessage(token, 1485743778301133291, id, "Stardance Demo but I edited the message!")
time.sleep(3)
deletemessage(token, 1485743778301133291, id)

logout(token)