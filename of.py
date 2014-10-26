import RPi.GPIO as GPIO
import time
import pygame

def buttonEvent (pin):
	global s
	print("Falling edge detected")
	s.play()

def main():
	global s
	pygame.mixer.init()
	s = pygame.mixer.Sound("Explosion.wav")
	
	GPIO.setmode(GPIO.BCM)

	GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

	GPIO.add_event_detect(18, GPIO.FALLING, bouncetime=300)
	GPIO.add_event_callback(18,buttonEvent)
	while True:
		time.sleep(150)
		print("Running...")
if __name__=="__main__":
	main()
