from sltfluxpy import *
import os
from dotenv import load_dotenv
import time
import requests
from PIL import Image
from io import BytesIO

load_dotenv()
token = os.getenv("FLUXTOKEN")

def render_image(url, width=60):
    response = requests.get(url)
    response.raise_for_status()

    img = Image.open(BytesIO(response.content)).convert("RGB")

    height = int(img.height * width / img.width / 2.5)
    img = img.resize((width, height * 2))

    pixels = img.load()

    for y in range(0, img.height, 2):
        for x in range(img.width):
            r1, g1, b1 = pixels[x, y]
            r2, g2, b2 = pixels[x, y + 1]

            print(
                f"\033[38;2;{r1};{g1};{b1}m"
                f"\033[48;2;{r2};{g2};{b2}m▀",
                end=""
            )

        print("\033[0m")

render_image(getuserpfp(token, 1555104919277535232),width=80)
