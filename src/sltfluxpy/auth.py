import requests
from datetime import datetime, timedelta, timezone

def login(email, password):
    response = requests.post("https://web.fluxer.app/api/v1/auth/login", headers={"Content-Type": "application/json", "Origin": "https://web.fluxer.app"}, json={"email": email,"password": password})
    return(response.json())