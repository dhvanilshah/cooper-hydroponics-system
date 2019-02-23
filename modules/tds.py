import busio
import digitalio
import board
import statistics
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
# configurable variables
NUM_SAMP = 30

#set up  the connection
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
cs = digitalio.DigitalInOut(board.D24)
mcp = MCP.MCP3008(spi, cs)

#set up the port for the tds sensor -- possibly change it to be config'd within
# config.py but for now:
# Connect TDS to MCP3008 CH0
# Connect CS from MCP3008 to Pi GP24
channel = AnalogIn(mcp, MCP.P0)

#Read Sample values into an array
def getTDS(temp):
	samp = [];
	for i in range(NUM_SAMP-1):
		samp.append(channel.voltage)
	# get the median value of the array to elimintae any outliers
	median = statistics.median(samp);
	#add temperature compensation coefficient to median
	comp_coef = 1.0 + 0.02*(float(temp) - 25.0)
	comp_med = median/comp_coef
	# convert the median value into a tds reading
	tds = (133.42 *  float(comp_med)**3 - 255.86 * float(comp_med)**2 + 857.39 * float(comp_med)) * 0.5
	#tds2 = (133.42 *  float(median)**3 - 255.86 * float(median)**2 + 857.39 * float(median)) * 0.5
	#print(samp);
	#print('Median is: ' + str(median))
	#print('TDS Comp is: ' + str(tds))
	#print('TDS Uncomp is: ' +  str(tds2))
	return tds

# -------- TEST CODE BELOW ---------------------------

#getTDS(25)
#getTDS(30)

#while True:
#    print('Raw ADC Value: ', channel.value)
#    print('ADC Voltage: ' + str(channel.voltage) + 'V')
#    time.sleep(0.5)

