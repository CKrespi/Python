import pygame
import time

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('ex21.mp3')
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    time.sleep(1)