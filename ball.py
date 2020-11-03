import pygame
class Ball:
    #class variables
    RADIUS = 10
    def __init__(self, x, y, vx, vy, screen, fgcolor, bgcolor, CONSTS):
        #instance varaibles
        self.x = x
        self.y = y
        self.screen = screen
        self.vx = vx
        self.vy = vy
        self.fgcolor = fgcolor
        self.bgcolor = bgcolor
        self.CONSTS = CONSTS
    
    def show(self, color):
        pygame.draw.circle(self.screen, color,(self.x, self.y), self.RADIUS)
    
    def update(self):
        #new position = old position + delta position (velocity)
        #delete old ball
        self.show(self.bgcolor)
        px = self.x + self.vx
        py = self.y + self.vy
       

        #print(self.CONSTS.BORDER)
        #TO-DO:
        #Check if I'm collision (wall position):
            #flip the velocity
        #Left Wall
        if px < self.CONSTS.BORDER + self.RADIUS:
            self.vx = -self.vx
        #Top Wall
        if py > 15 + self.RADIUS:
                    self.vy = -self.vy
        #Bottom Wall
        if py < (self.CONSTS.HEIGHT - self.CONSTS.BORDER) - self.RADIUS :
                    self.vy = -self.vy
        
        self.x = self.x + self.vx
        self.y = self.y + self.vy
        self.show(self.fgcolor)