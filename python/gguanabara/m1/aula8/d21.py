# Faça um programa em Puthon que abra e reproduza um arquivo mp3.

import pygame

pygame
pygame.init()
pygame.mixer.music.load('d21.mp3')
pygame.mixer.music.play()
pygame.event.wait()