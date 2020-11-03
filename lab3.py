from paddle import Paddle
from ball import Ball
from collections import namedtuple

import pygame
import random
def main():
    pygame.init()
    pygame.display.set_caption("my pong")

    WIDTH = 800
    HEIGHT = 400
    BORDER = 15
    VELOCITY = 5
    FPS = 30

    MyConstants = namedtuple("MyConstants", ["WIDTH", "HEIGHT", "BORDER", "VELOCITY", "FPS"])   

    CONSTS = MyConstants(WIDTH, HEIGHT, BORDER, VELOCITY, FPS)
    print(CONSTS.BORDER)

    #surface
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    screen.fill((0,0,0))
    # double buffering: stage updates together; update them at once.
    # avoids flickering it
    pygame.display.update()

    #Walls
    #Rect(surface, color, rect) -> Rect
    #Rect((left,top), (width, height)) -> Rect
    wallColor = pygame.Color("white")
    ballColor = pygame.Color("white")
    bgColor = pygame.Color("black")

    #top wall
    pygame.draw.rect(screen, wallColor, pygame.Rect((0,0),(WIDTH,BORDER)))
    #left wall
    pygame.draw.rect(screen, wallColor, pygame.Rect((0,0),(BORDER,HEIGHT)))
    #bottom wall
    pygame.draw.rect(screen, wallColor, pygame.Rect((0,HEIGHT-BORDER),(WIDTH,BORDER)))
    #Ball Init
    x0 = WIDTH - Ball.RADIUS
    y0 = HEIGHT // 2

    if random.random() < 0.5:
        signNumber = 1
    else:
        signNumber = -1

    vx0 = -VELOCITY
    vy0 = signNumber * VELOCITY
    
    #TO-DO: +/- 45 degree/random

    b0 = Ball(x0,y0, vx0, vy0, screen, ballColor, bgColor, CONSTS)
    b0.show(ballColor)

    pygame.display.update()

    # Define a variable to control the main loop
    running = True
    clock = pygame.time.Clock()

    # main loop
    while running:
        # event handling, gets all events from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
        pygame.display.update()
        clock.tick(FPS)
        #Ball
        b0.update()
                
if __name__ == "__main__":
    main()

#TO-DO: push lab3.py to git with 2 TO-DOs +
# capture a gif and include in your README.md
#GID: shows collisiton with the ball and rand start