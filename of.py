import RPi.GPIO as GPIO
import time
import pygame
import random
import glob


def buttonEvent (pin):
	global s
	print(GPIO.input(18))
	if(GPIO.input(18)):
		print("Falling edge detected")
		rand = random.randint(0, len(s))
                s[rand].play()

def main():
	global s
	pygame.mixer.init()
	random.seed(time.time())
        pygame.mixer.init()

        s = []
        for filename in x:
            s.append(pygame.mixer.Sound(filename))
            print("loaded: {}".format(filename))
	
	GPIO.setmode(GPIO.BCM)

	GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

	GPIO.add_event_detect(18, GPIO.FALLING, callback=buttonEvent, bouncetime=150)
	while True:
		time.sleep(150)
		print("Running...")
if __name__=="__main__":
	main()
