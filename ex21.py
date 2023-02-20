#Tocando um MP3
import pygame
pygame.init()
pygame.mixer.music.load('aula3.mp3')
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    pass
