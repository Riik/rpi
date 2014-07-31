import time
import os
# import function that gets temperature data from other file
from news import get_news

class news_daemon():
    
    stdin_path = '/dev/null'
    stdout_path = '/tmp/stdout.log'
    stderr_path = '/tmp/stderr.log'
    pidfile_path = '/var/lock/disp_news.pid'
    pidfile_timeout = 200
    
    def run(self):
        self.news_displayer()

    def news_displayer(self):
        refreshtime = 60
        # clear screen
        os.system('bw_tool -I -a 94 -D /dev/i2c-1 -w 10:0')
        # set contrast 
        os.system('bw_tool -I -a 94 -D /dev/i2c-1 -w 12:000f')
        # set brightness
        os.system('bw_tool -I -a 94 -D /dev/i2c-1 -w 13:0080')
        while 1:
           	t = get_news()
           	print(t[0])
           	print(t[1])
           	# clear screen
           	os.system('bw_tool -I -a 94 -D /dev/i2c-1 -w 10:0')
           	# write first line
           	os.system('bw_tool -I -a 94 -D /dev/i2c-1 -t {}'.format(t[0]))
           	# set cursor to new line
           	os.system('bw_tool -I -a 94 -D /dev/i2c-1 -w 11:20')
           	# print weather data
           	os.system('bw_tool -I -a 94 -D /dev/i2c-1 -t {}'.format(t[1]))
           	time.sleep(refreshtime)
