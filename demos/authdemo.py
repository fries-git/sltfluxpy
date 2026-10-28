import dotenv
import os
from sltfluxpy import *

dotenv.load_dotenv()

email, password = os.getenv("EMAIL"), os.getenv("PASSWORD")
settoken(login(email, password)["token"])
sendmessage(1550942247631982595, "test")
logout()