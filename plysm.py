import glob
import random
import time
import pygame

x = glob.glob('./wavjes/*.wav')
print("Number of files found in /wavjes:")
print(len(x))

random.seed(time.time())
pygame.mixer.init()

s = []
for filename in x:
    s.append(pygame.mixer.Sound(filename))
    print("loaded: {}".format(filename))
for i in xrange(5):
    rand = random.randint(0, len(s))
    s[rand].play()
    time.sleep(3)

