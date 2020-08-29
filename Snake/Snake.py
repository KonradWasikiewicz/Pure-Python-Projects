#https://www.youtube.com/watch?v=CD4qAhfFuLo   # 18:39 powinna juz si eplansza wyswietlac 
https://pastebin.com/embed_js/jB6k06hG 


import math
import random 
import pygame
import tkinter as tk
from tkinter import messagebox

class cube(object):
    rows = 20 
    w = 500
    def __init__(self, start, dirnx = 1, dirny = 0, color = (255,0,0)):
        self.pos = start
        self.dirnx = 1
        self.dirny = 0
        self.color = color
    def move(self, dirnx, driny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)
    def draw(self, surface, eyes = False):
        dis = self.w // self.rows
        i = self.pos[0]
        j = self.pos[1]

        pygame.draw.rect(surface, self.color, (i*dis+1,j*dis+1, dis-2, dis-2))
        if eyes:
            centre = dis//2
            radius = 3
            circleMiddle = (i*dis+centre-radius,j*dis+8)
            circleMiddle2 = (i*dis + dis -radius*2, j*dis+8)
            pygame.draw.circle(surface, (0,0,0), circleMiddle, radius)
            pygame.draw.circle(surface, (0,0,0), circleMiddle2, radius)

class snake(object):
    body = []
    turns = {}
    def __init_(self, color, pos):
        self.color = color
        self.head = cube(pos)
        self.body.append(self.head)
        self.dirnx = 0    #keeping track of what direction are we moving 
        self.dirny = 1

    def move(self):                   #chyba tutaj jest jakis blad w kodzie, bo jak masz jakies 2-3 cubes to wysjakuje blad jak snake idzie w prawo a klikniesz w lewo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            keys = pygame.key.get_pressed()

            for key in keys:                       #defining directions
                if keys[pygame.K_LEFT]:             
                    self.dirnx = -1 
                    self.dirny = 0 
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]  #adding key which is the current position of the head of the snake 

                if keys[pygame.K_RIGHT]:                    
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
        
        for i, c in enumerate(self.body):
            p = c.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0],turn[1])
                if i == len(self.body)-1:
                    self.turns.pop(p)
            else:
                if c.dirnx == -1 and c.pos[0] <= 0: c.pos = (c.rows-1, c.pos[1])
                elif c.dirnx == 1 and c.pos[0] >= c.rows-1: c.pos = (0,c.pos[1])
                elif c.dirny == 1 and c.pos[1] >= c.rows-1: c.pos = (c.pos[0], 0)
                elif c.dirny == -1 and c.pos[1] <= 0: c.pos = (c.pos[0],c.rows-1)
                else: c.move(c.dirnx,c.dirny)
       

    def reset(self, pos):
        self.head = cube(pos)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.dirnx = 0
        self.dirny = 1
    def addTail(self):
        tail = self.body[-1]
        dx, dy = tail.dirnx, tail.dirny
 
        if dx == 1 and dy == 0:
            self.body.append(cube((tail.pos[0]-1,tail.pos[1])))

            
    def draw(self,surface):
        pass

 
def drawGrid(w, rows, surface):
    sizeBtwn = w // rows  #how big each square in the grid is going to be 
    x = 0 
    y = 0
    for l in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn

        pygame.draw.line(suface,(255,255,255), (x,0),(x,w)) #drawing a white line
        pygame.draw.line(suface,(255,255,255), (0,y),(w,y)) #drawing a white 
                

def redrawWindow(surface):
    global rows, width, s, snack
    surface.fill((0,0,0))
    s.draw(surface)
    snack.draw(surface)
    drawGrid(width,rows, surface)
    pygame.display.update()
    
def randomFood(rows, items):
    pass

def message_box(subject, content):
    pass


def main():
    width = 500
    rows = 20
    win = pygame.display.set_mode((width, width))
    s = snake((255,0,0), (10,10))
    flag = True

    clock = pygame.time.Clock()

    while flag:
        pygame.time.delay(50)
        clock.tick(10)
        redrawWindow(win)


main()
