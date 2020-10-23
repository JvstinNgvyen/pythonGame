import pygame
pygame.init()
pygame.display.set_caption("my pong")

WIDTH = 800
HEIGHT = 400
#surface
screen = pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill((0,0,0))
# double buffering: stage updates together; update them at once.
# avoids flickering
pygame.display.update()

#Walls
#Rect(surface, color, rect) -> Rect
#Rect((left,top), (width, height)) -> Rect
wallColor = pygame.Color("white")
BORDER = 15
#top wall
pygame.draw.rect(screen, wallColor, pygame.Rect((0,0),(WIDTH,BORDER)))
#left wall
pygame.draw.rect(screen, wallColor, pygame.Rect((0,0),(BORDER,HEIGHT)))
#bottom wall
pygame.draw.rect(screen, wallColor, pygame.Rect((0,HEIGHT-BORDER),(WIDTH,BORDER)))

pygame.display.update()

# Define a variable to control the main loop
running = True

# main loop
while running:
    # event handling, gets all events from the event queue
    for event in pygame.event.get():
        # only do something if the event is of type QUIT
        if event.type == pygame.QUIT:
            # change the value to False, to exit the main loop
            running = False


