from modules.relay_lib import *
import os, sys, inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import settings

def lights_on():
	relay_on(settings.LIGHT_RELAY)

def lights_off():
	relay_off(settings.LIGHT_RELAY)
