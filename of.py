import RPi.GPIO as GPIO
import time
import pygame

def buttonEvent (pin):
	global s
	print("callback called")
	x = 0
	time.sleep(.050)
	for i in xrange(5):
		x += GPIO.input(18)	
	print(x)
	if x > 2:
		print("Fridge opened")
		s.play()

def main():
	global s
	pygame.mixer.init()
	s = pygame.mixer.Sound("Explosion.wav")
	s.play()	
	GPIO.setmode(GPIO.BCM)

	GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

	GPIO.add_event_detect(18, GPIO.FALLING, callback=buttonEvent, bouncetime=200)
	while True:
		time.sleep(.50)

if __name__=="__main__":
	main()
