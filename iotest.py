import RPi.GPIO as GPIO
import time

def main():

	pygame.mixer.init()
	
	GPIO.setmode(GPIO.BCM)

	GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	while True:
		time.sleep(50)
		print(GPIO.input(18)
		print("Running...")
if __name__=="__main__":
	main()
