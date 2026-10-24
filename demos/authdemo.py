import dotenv
import os
from sltfluxpy import *

dotenv.load_dotenv()

email, password = os.getenv("EMAIL"), os.getenv("PASSWORD")
login = login(email, password)
usertoken = login["token"]
changestatus(usertoken, "LOGINS WORK IN MY PYTHON LIB", 1)