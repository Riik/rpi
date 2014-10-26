import RPi.GPIO as GPIO
import time
import pygame

def buttonEvent (pin):
	global time_stamp
	if time.time() - time_stamp > 0.5:
		print("Starting music")
		s = pygame.mixer.Sound("Explosion.wav")
		s.play()
		time_stamp = time.time()


def main():
	global time_stamp
	time_stamp  = time.time()
	pygame.mixer.init()
	
	GPIO.setmode(GPIO.BCM)

	GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

	GPIO.add_event_detect(18, GPIO.FALLING)
	GPIO.add_event_callback(18,buttonEvent)
	while True:
		time.sleep(150)
		print("Running...")
if __name__=="__main__":
	main()
