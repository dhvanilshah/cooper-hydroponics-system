from api.queries import recordReadings
from modules.tds import getTDS
from modules.lights import lights_on, lights_off
from modules.water_temp import read_temp
from modules.liq_level import get_level
import time

wat_lvl = get_level()
if wat_lvl:
    print("Water Level Sufficient")
else:
    print("Water Level Low")

temps = read_temp()
temp_c = temps[0]
temp_f = temps[1]

print("Water Temperature is: " + str(temp_f))

tds = getTDS(temp_c)
print("TDS is: " + str(tds) + " PPM")

lights_on()
time.sleep(2)
lights_off()

result = recordReadings(temp_f, tds, wat_lvl)
print(result)
