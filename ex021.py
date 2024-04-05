# Tocando musica MP3

# Importando biblioteca pygame
import pygame

# Iniciando o pygame
pygame.init()

# Importando a musica que irá tocar
pygame.mixer.music.load('ex021.mp3')

# Tocando a musica
pygame.mixer.music.play()

# O pygame atualizou e a função ".play" é necessario usar o
# "input()" na linha abaixo.
input()
pygame.event.wait()
