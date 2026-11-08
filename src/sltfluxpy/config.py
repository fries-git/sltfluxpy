token = None
global api
api = "https://fluxer.app/api/v1"
global gatewayapi
gatewayapi = "wss://gateway.fluxer.app?v=1&encoding=json"
advanced_logging = False
from .log import *
from .instance import wellknown

def automaticapi(instanceurl):
    data = wellknown(instanceurl)
    endpoints = data["endpoints"]
    global api, gatewayapi

    api = f"{endpoints['api_public']}/v1"
    gatewayapi = f"{endpoints["gateway"]}?v=1&encoding=json"

    if advanced_logging:
        success(f"API found as: {api}")
        success(f"Gateway found as: {gatewayapi}")

def settoken(tokenin):
    global token
    token = tokenin

def setapi(apiin):
    global api
    api = apiin

def setgateway(apiin):
    global gatewayapi
    gatewayapi = apiin

def doadvancedlogging(boolean):
    if isinstance(boolean, bool):
        global advanced_logging
        advanced_logging = boolean
        if boolean:
            success("Advanced Debug Mode Activated")
        if not boolean:
            error("Advanced Debug Mode Deactivated")
    else:
        return("Non-boolean passed")