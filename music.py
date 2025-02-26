import pygame

def play_song():
    pygame.init()  # inicializa o pygame
    pygame.mixer.music.load('song.mp3') # carrega a música
    pygame.mixer.music.play(-1) # toca a música em loop



