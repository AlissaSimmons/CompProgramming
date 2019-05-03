#import statements
import pygame
pygame.init()

# create display
background_color = (240,255,255)
(width,height) = (800,500)
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Platonic Solids')
screen.fill(background_color)
pygame.display.flip()

# Drawing instructions for each shape


#Keeps the program open
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False