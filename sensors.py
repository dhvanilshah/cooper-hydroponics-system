from api.queries import recordTemp
from modules.tds import getTDS
from modules.lights import lights_on, lights_off
from modules.water_temp import read_temp
from modules.liq_level import get_level
from settings import WATER_TEMP, WATER_LEVEL, TDS, PH, SALINITY, HUMIDITY
import time
import schedule
