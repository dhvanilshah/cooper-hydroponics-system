import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)

def get_level():
    level =  GPIO.input(17)
    return level
# ------------ TESTING CODE BELOW ------------------
#while True:
#   get_level()
