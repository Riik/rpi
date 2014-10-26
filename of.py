import RPi.GPIO as GPIO
import time
import pygame
import random
import glob


def buttonEvent (pin):
	global s, music

	time.sleep(0.05)
	if (GPIO.input(18)):
		music.stop()
		print("Playing music")
		music  = s[random.randint(0, len(s))]
 		music.play()
	else:
		music.stop()

def main():
	global s, music
	pygame.mixer.init()
	random.seed(time.time())
        pygame.mixer.init()

	x = glob.glob('./wavjes/*.wav')
        s = []
        for filename in x:
            s.append(pygame.mixer.Sound(filename))
            print("loaded: {}".format(filename))
	print("Loaded {} files".format(len(s)))
	music = s[0]
	music.play()	

	GPIO.setmode(GPIO.BCM)

	GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

	GPIO.add_event_detect(18, GPIO.FALLING, callback=buttonEvent, bouncetime=150)
	while True:
		time.sleep(150)
		print("Running...")
if __name__=="__main__":
	main()
