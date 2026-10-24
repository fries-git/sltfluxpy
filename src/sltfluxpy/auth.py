import requests
import altcha as al
import base64
import json

def login(email, password):
    js = {"email": email,"password": password}
    response = requests.post("https://web.fluxer.app/api/v1/auth/login", headers={"Content-Type": "application/json", "Origin": "https://web.fluxer.app"}, json=js)
    resp = response.json()
    resp = resp["altcha_challenge"]
    
    challenge = al.Challenge.from_dict(resp)
    solve = al.solve_challenge(challenge)

    token = base64.b64encode(json.dumps({"challenge": resp,"solution": {"counter": solve.counter,"derivedKey": solve.derived_key,"time": solve.time}}).encode()).decode()

    response = requests.post("https://web.fluxer.app/api/v1/auth/login", headers={"Content-Type": "application/json", "Origin": "https://web.fluxer.app", "X-Captcha-Token": token}, json=js)
    return (response.json())

def logout(token):
    response = requests.post("https://web.fluxer.app/api/v1/auth/logout", headers={"Authorization": token, "Content-Type": "application/json", "Origin": "https://web.fluxer.app"})
    return("Logged out.")