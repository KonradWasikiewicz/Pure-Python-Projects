#https://www.youtube.com/watch?v=CD4qAhfFuLo    
#https://pastebin.com/embed_js/jB6k06hG 

#features: leaderboard, score at the top, bug z tym zawracaniem 

import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox

#RGB color scale numbers
blue = (51,80,212)
white = (252, 252, 252)
red = (255,0,0)
green = (51,161,66)

class cube(object):
    rows = 20
    w = 500
    def __init__(self, start, dirnx = 1, dirny = 0, color = blue):  
        self.pos = start
        self.dirnx = 1  #makes snake go right at the beginning 
        self.dirny = 0
        self.color = color
        
    def move(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)
 
    def draw(self, surface, eyes=False):
        dis = self.w // self.rows
        i = self.pos[0]
        j = self.pos[1]
 
        pygame.draw.rect(surface, self.color, (i*dis+1,j*dis+1, dis-2, dis-2)) #draws the cube inside the grid lines 

        if eyes: 
            centre = dis//2
            radius = 3
            circleMiddle = (i * dis + centre - radius*2,j*dis+10)   #eyes position 
            circleMiddle2 = (i * dis + dis - radius*2, j*dis+10)
            pygame.draw.circle(surface, white, circleMiddle, radius) #white eyes drawn
            pygame.draw.circle(surface, white, circleMiddle2, radius)
       
class snake(object):
    body = []   #we add to that as we eat 
    turns = {}  #we add to that as we turn 
    def __init__(self, color, pos):
        self.color = color
        self.head = cube(pos)   #head is defined as a function of cube 
        self.body.append(self.head)
        self.dirnx = 0
        self.dirny = 1
 
    def move(self):   #defining how the body follows snake's head 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   #makes quitting possible via clicking the upper right red button 
                pygame.quit()
 
            keys = pygame.key.get_pressed() #gets a dictionary of all the key values and if they were pressed
 
            for key in keys:   #defining what is going to happen when we hit defined keys 
                if keys[pygame.K_LEFT]:
                    self.dirnx = -1  #point (0,0) is in the upper left corner, so -1 takes us closer to 0. Others per analogiam
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny] #we are adding a key to the dict above that is the current pos of the head of our snake
 
                elif keys[pygame.K_RIGHT]:
                    self.dirnx = 1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
 
                elif keys[pygame.K_UP]:
                    self.dirnx = 0
                    self.dirny = -1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
 
                elif keys[pygame.K_DOWN]:
                    self.dirnx = 0
                    self.dirny = 1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
 
        for i, c in enumerate(self.body):  #i = index, c = cube type object 
            p = c.pos[:]    
            if p in self.turns:   #we are going to move to the direction describes by 'self.turns'
                turn = self.turns[p]
                c.move(turn[0],turn[1])
                if i == len(self.body)-1: 
                    self.turns.pop(p)
            else:  #what to do when we are reaching the end of the screen -> transfer to the other side of the map
                if c.dirnx == -1 and c.pos[0] <= 0: c.pos = (c.rows-1, c.pos[1])
                elif c.dirnx == 1 and c.pos[0] >= c.rows-1: c.pos = (0,c.pos[1])
                elif c.dirny == 1 and c.pos[1] >= c.rows-1: c.pos = (c.pos[0], 0)
                elif c.dirny == -1 and c.pos[1] <= 0: c.pos = (c.pos[0],c.rows-1)
                else: c.move(c.dirnx, c.dirny) #if not at the end, move forward  
       
 
    def reset(self, pos):
        self.head = cube(pos)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.dirnx = 0
        self.dirny = 1
 
 
    def addCube(self):
        tail = self.body[-1]
        dx, dy = tail.dirnx, tail.dirny
 
        if dx == 1 and dy == 0:   #add tail at the end, to the opposite direction of snake's move 
            self.body.append(cube((tail.pos[0]-1,tail.pos[1])))
        elif dx == -1 and dy == 0:
            self.body.append(cube((tail.pos[0]+1,tail.pos[1])))
        elif dx == 0 and dy == 1:
            self.body.append(cube((tail.pos[0],tail.pos[1]-1)))
        elif dx == 0 and dy == -1:
            self.body.append(cube((tail.pos[0],tail.pos[1]+1)))
 
        self.body[-1].dirnx = dx
        self.body[-1].dirny = dy
       
 
    def draw(self, surface):
        for i, c in enumerate(self.body):
            if i ==0:
                c.draw(surface, True) #if True, draw eyes at the first cube 
            else:
                c.draw(surface)
 
 
def drawGrid(w, rows, surface):
    sizeBtwn = w // rows
    x = 0
    y = 0
    for l in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn
 
        pygame.draw.line(surface, white, (x,0),(x,w))  #draws two lines, horizontal and vertical 
        pygame.draw.line(surface, white, (0,y),(w,y))  
 
def redrawWindow(surface):
    surface.fill(green)  
    s.draw(surface)
    snack.draw(surface)
    drawGrid(width, rows, surface)
    pygame.display.update()
 
 
def randomSnack(rows, item):
 
    positions = item.body
 
    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)
        if len(list(filter(lambda z:z.pos == (x,y), positions))) > 0:  #making sure snack won't be added at the top of the snake 
            continue
        else:
            break
       
    return (x,y)
 
 
def message_box(subject, content):
    root = tk.Tk()
    root.attributes("-topmost", True) #window comes up top on everything 
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass
 
#mainloop 
def main():
    global width, rows, s, snack
    width = 500
    rows = 20
    win = pygame.display.set_mode((width, width))    # tutaj umiejscowic score wyzej 
    s = snake(blue, (10,10))  #snake's starting position  
    snack = cube(randomSnack(rows, s), color = red)
    run = True
    clock = pygame.time.Clock()
   
    while run:
        pygame.time.delay(40)  #speed control  the lower the faster
        clock.tick(10)     #speed control      the lower the slower
        s.move()
        if s.body[0].pos == snack.pos:
            s.addCube()
            snack = cube(randomSnack(rows, s), color = red)
 
        if s.body[0].pos in list(map(lambda z:z.pos,s.body[1:])):
            message_box('You Lost!', 'Your score is {}'.format(len(s.body)))
            s.reset((10,10))
            break
            
        redrawWindow(win) 
 
main()