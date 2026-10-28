import requests
import altcha as al
import base64
import json
from . import config
import time

def login(email, password):
    js = {"email": email,"password": password}
    response = requests.post("https://web.fluxer.app/api/v1/auth/login", headers={"Content-Type": "application/json", "Origin": "https://web.fluxer.app"}, json=js)
    resp = response.json()
    resp = resp["altcha_challenge"]
    
    challenge = al.Challenge.from_dict(resp)
    solve = al.solve_challenge(challenge)

    token = base64.b64encode(json.dumps({"challenge": resp,"solution": {"counter": solve.counter,"derivedKey": solve.derived_key,"time": solve.time}}).encode()).decode()

    time.sleep(1)

    response = requests.post("https://web.fluxer.app/api/v1/auth/login", headers={"Content-Type": "application/json", "Origin": "https://web.fluxer.app", "X-Captcha-Token": token}, json=js)
    config.settoken(response.json()["token"])
    return (response.json())

def logoutmanual(token):
    response = requests.post("https://web.fluxer.app/api/v1/auth/logout", headers={"Authorization": token, "Content-Type": "application/json", "Origin": "https://web.fluxer.app"})
    return("Logged out.")

def logout():
    token = config.token
    response = requests.post("https://web.fluxer.app/api/v1/auth/logout", headers={"Authorization": token, "Content-Type": "application/json", "Origin": "https://web.fluxer.app"})
    return("Logged out.")