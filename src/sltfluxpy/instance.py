import requests

def wellknown(apiin):
    response = requests.get(f"{apiin}/.well-known/fluxer")
    return response.json()

def status():
    response = requests.get("https://fluxerstatus.com/v3/summary.json")
    return response.json()