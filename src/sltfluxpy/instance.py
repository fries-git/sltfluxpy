import requests

def wellknown():
    response = requests.get("https://web.fluxer.app/api/v1/.well-known/fluxer")
    return response.json()

def status():
    response = requests.get("https://fluxerstatus.com/v3/summary.json")
    return response.json()