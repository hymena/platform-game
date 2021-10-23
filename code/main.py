import pygame
from pygame.constants import QUIT
from settings import *
from level import Level
from game_data import level_0
#Pygame setup 


pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Platform game')
clock = pygame.time.Clock()
level = Level(level_0, screen) 

#Main game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
    
    screen.fill('grey')
    level.run()
    
    pygame.display.update()
    clock.tick(FPS)

