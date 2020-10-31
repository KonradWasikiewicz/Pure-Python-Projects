"""problemy:

ogarnij dodaj timer

* nie przerywa po nacisnieciu czerwonego buttona
* załadowac inne algorytmy
*cos sie wyjebywuje jak skonczy

list selection - do wyboru algorytmu
dodać czas i napis "done!"
zmiana układu graficxznego (linie do dołu, inne miejsce na napisy)
algos do osobnych plikow i pol dnia z dostosowywwaniem ich
"""


# main file, responsible for visualizing algos defined in other files

import os
import sys
import time

import random
import pygame

# main window size and fill
WIDTH = 1000
HEIGHT = 620

screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill((255, 255, 255))

# title and icon settings
pygame.display.set_caption("Sorting Alogs")

# setting up a relative path for the icon
base_path = os.path.dirname(__file__)
icon_path = os.path.join(base_path, "icon.png")
img = pygame.image.load(icon_path)

pygame.display.set_icon(img)


RECORDS = 89                                # defining number of RECORDS to be sorted
ARRAY = [0]*RECORDS                         # pre-defining the array as a list of x RECORDS with height of 0
ARR_COLOR = [(0, 0, 0)]*RECORDS
COLOR = [(46, 63, 222), (255, 255, 8), (255, 0, 0), (97, 223, 0)] # color palette [blue, yellow, red, green]

pygame.font.init()                          # initializing text, so that it can be shown within the app
fnt = pygame.font.SysFont("calibri", 25)

# generating array
def generate_arr():
    for i in range(1, RECORDS):
        ARR_COLOR[i] = COLOR[0]                 # defining array color within pre-defined palette
        ARRAY[i] = random.randrange(1, 100) # randomly generating height of each record

generate_arr()

def refill():
    screen.fill((255, 255, 255))
    draw()
    pygame.display.update()
    pygame.time.delay(8)                    # setting number of milliseconds in which each operation is being done

def check_events():                         # checking if window closing request was made
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

# Sorting Algo:Merge sort
def mergesort(ARRAY, left, right):
    mid = (left + right)//2
    if left < right:
        mergesort(ARRAY, left, mid)
        mergesort(ARRAY, mid + 1, right)
        merge(ARRAY, left, mid, mid + 1, right)
def merge(ARRAY, x1, y1, x2, y2):
    i = x1
    j = x2
    temp = []
    pygame.event.pump()
    while i <= y1 and j <= y2:
        ARR_COLOR[i] = COLOR[1]
        ARR_COLOR[j] = COLOR[1]
        refill()
        ARR_COLOR[i] = COLOR[0]
        ARR_COLOR[j] = COLOR[0]
        if ARRAY[i] < ARRAY[j]:
            temp.append(ARRAY[i])
            i += 1
        else:
            temp.append(ARRAY[j])
            j += 1
    while i <= y1:
        ARR_COLOR[i] = COLOR[1]
        refill()
        ARR_COLOR[i] = COLOR[0]
        temp.append(ARRAY[i])
        i += 1
    while j <= y2:
        ARR_COLOR[j] = COLOR[1]
        refill()
        ARR_COLOR[j] = COLOR[0]
        temp.append(ARRAY[j])
        j += 1
    j = 0
    for i in range(x1, y2 + 1):
        pygame.event.pump()
        ARRAY[i] = temp[j]
        j += 1
        ARR_COLOR[i] = COLOR[2]
        refill()
        if y2-x1 == len(ARRAY)-2:
            ARR_COLOR[i] = COLOR[3]
        else:
            ARR_COLOR[i] = COLOR[0]


def draw():
    txt1 = fnt.render("Press ENTER to start sorting.", 1, (0, 0, 0))    # rendering the text
    screen.blit(txt1, (680, 50))                                        # setting its position

    txt2 = fnt.render("Press 'W' for a new array.", 1, (0, 0, 0))
    screen.blit(txt2, (680, 80))

    txt3 = fnt.render("Algorithm used: Merge Sort", 1, (0, 0, 0))
    screen.blit(txt3, (680, 200))

#    txt4 = fnt.render("Time passed: {:.2f}".format(time.time() - algorithm.start_time), 1, (0, 0, 0))                #OPISZ CZAS !!!!!!!!!!!!!!!!!!
#    screen.blit(txt4, (680, 250))

    record_width = 6                                                   # width of a single record
    space_btwn_rec = 7                                                 # space between records
    height_rec = 6.5                                                   # height of a single record

    # drawing the array values as lines
    for i in range(1, RECORDS):
        pygame.draw.line(screen, ARR_COLOR[i], (0, space_btwn_rec * i-3), (ARRAY[i]*height_rec, space_btwn_rec * i-3), record_width)
      # pygame.draw.line syntax: line(surface, color, start_pos, end_pos, width)

# boolean variable to run the program in while loop
RUNNING  = True

# main loop
while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # setting up a possibility to quit while not running
            RUNNING = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                generate_arr()
            if event.key == pygame.K_RETURN:
                mergesort(ARRAY, 1, len(ARRAY)-1)            #KLUCZOWE DLA DEFINICJI ALGOS
        draw()
        pygame.display.update()

pygame.quit()
