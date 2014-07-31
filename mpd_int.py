from mpd import MPDClient
import time
import os

client = MPDClient()
client.timeout = 30
client.idletimeout = None
client.connect("localhost", 6600)
i = 0
oldsong = client.currentsong()
while i < 10:
	song = client.currentsong()
	if(song != oldsong):
		oldsong = song
		os.system('bw_tool -I -a 94 -D /dev/i2c-1 -w 10:0')
		os.system('bw_tool -I -a 94 -D /dev/i2c-1 -t {}'.format(song["title"]))
		os.system('bw_tool -I -a 94 -D /dev/i2c-1 -w 11:20')
		os.system('bw_tool -I -a 94 -D /dev/i2c-1 -t {}'.format(song["artist"]))
		print(song["artist"])
		print(song["title"])
	time.sleep(2)
	i = i + 1
	print(i)
client.disconnect()
