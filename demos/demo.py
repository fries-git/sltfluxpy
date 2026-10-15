from sltfluxpy import *
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("FLUXTOKEN")

changebio(token, "Hello!")
changestatus(token, "Yo its me, fries!", 10000)

changeaccentcolor(token, "#456e1f")