from mpd import MPDClient
from daemon import runner
import time
import os

class MPD_interface:
        
    stdin_path = '/dev/null'
    stdout_path = '/tmp/stdout.log'
    stderr_path = '/tmp/stderr.log'
    pidfile_path = '/var/lock/mpd_int.pid'
    pidfile_timeout = 200
        
    def __init__(self):
        
        # conenct client and set values
        client = MPDClient()
        client.timeout = 30
        client.idletimeout = None
        client.connect("localhost", 6600)
        self.client = client
    
    def run(self):
        self.main_loop()
        
    def main_loop(self):
        # make local copy of client variable
        client = self.client
        # first read-out of current song
        # currentsong returns JSON message with info about song
        oldsong = client.currentsong()
        while 1:
                # read current song, if the song changed execute loop
           	song = client.currentsong()
           	if(song != oldsong):
          		oldsong = song
          		# clear screen
          		os.system('bw_tool -I -a 94 -D /dev/i2c-1 -w 10:0')
          		# write artist name
          		os.system('bw_tool -I -a 94 -D /dev/i2c-1 -t {}'.format(song["artist"]))
          		# set cursor to line 2
          		os.system('bw_tool -I -a 94 -D /dev/i2c-1 -w 11:20')
          		# write title of song
          		os.system('bw_tool -I -a 94 -D /dev/i2c-1 -t {}'.format(song["title"]))
          		print(song["artist"])
          		print(song["title"])
           	time.sleep(2)
           	
    def __exit__(self):
        # on exit, disconnect the client
        self.client.disconnect()
        
app = MPD_interface()
daemon_runner = runner.DaemonRunner(app)
daemon_runner.do_action()
