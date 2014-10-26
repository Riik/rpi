import RPi.GPIO as GPIO
import time
import pygame
import random
import glob

class of_daemon():

        # some daeon stuff here 
        stdin_path = '/dev/null'
        stdout_path = '/tmp/stdout.log'
        stderr_path = '/tmp/stderr.log'
        pidfile_path = '/var/lock/disp_news.pid'
        pidfile_timeout = 200
        
        def buttonEvent (pin):
                global s, music
                # wait for switch to settle
                time.sleep(0.05)
                # check if door was opened or closed
                if (GPIO.input(18)):
                        music.stop()
                        print("Playing music")
                        music  = s[random.randint(0, len(s))]
                        music.play()
                else:
                        music.stop()

        def run(self):
                self.main()
        
        def main(self):
                global s, music
                pygame.mixer.init()
                random.seed(time.time())
                pygame.mixer.init()
                # index all files
                x = glob.glob('./wavjes/*.wav')
                s = []
                # load all files as pygame Sounds
                for filename in x:
                    s.append(pygame.mixer.Sound(filename))
                    print("loaded: {}".format(filename))
                print("Loaded {} files".format(len(s)))
                # init music global
                music = s[0]

                GPIO.setmode(GPIO.BCM)
                GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
                GPIO.add_event_detect(18, GPIO.FALLING, callback=buttonEvent, bouncetime=150)
                while True:
                        time.sleep(150)
                        print("Running...")
                        
if __name__=="__main__":
	run()
