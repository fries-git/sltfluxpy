token = None
advanced_logging = False
from .log import *

def settoken(tokenin):
    global token
    token = tokenin

def advancedlogging(boolean):
    if isinstance(boolean, bool):
        global advanced_logging
        advanced_logging = boolean
        if boolean:
            success("Advanced Debug Mode Activated")
        if boolean:
            error("Advanced Debug Mode Deactivated")
    else:
        return("Non-boolean passed")