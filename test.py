import time
import os
# import function that gets temperature data from other file
from temp import get_temperature
i = 0;
refreshtime = 30
temperature = get_temperature()
# clear screen
os.system('bw_tool -I -a 94 -D /dev/i2c-1 -w 10:0')
# set contrast 
os.system('bw_tool -I -a 94 -D /dev/i2c-1 -w 12:000f')
# set brightness
os.system('bw_tool -I -a 94 -D /dev/i2c-1 -w 13:0080')
while 1:
	# get system time in specified format
	timestr = time.strftime("%H:%M:%S")
	# reset cursor
        os.system('bw_tool -I -a 94 -D /dev/i2c-1 -w 11:00')
	# print time
	os.system('bw_tool -I -a 94 -D /dev/i2c-1 -t {0}'.format(timestr))
	i = i + 1
	if i > refreshtime:
	   i = 0
	   temperature = get_temperature()
	   # set cursor to new line
	   os.system('bw_tool -I -a 94 -D /dev/i2c-1 -w 11:20')
	   # print weather data
	   os.system('bw_tool -I -a 94 -D /dev/i2c-1 -t Delft, {} C'.format(temperature))
	time.sleep(1)


