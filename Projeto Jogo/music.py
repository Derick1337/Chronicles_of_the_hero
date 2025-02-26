import pygame.mixer as mixyy

def game_song():
    mixyy.init()
    mixyy.music.load("song.mp3")
    mixyy.music.play(loops=-1)

game_song()
