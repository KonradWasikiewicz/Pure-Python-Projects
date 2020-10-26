"""problemy:


* nie przerywa po nacisnieciu czerwonego buttona
* załadowac inne algorytmy
*cos sie wyjebywuje jak skonczy

list selection - do wyboru algorytmu
dodać czas i napis "done!"
zmiana układu graficxznego (linie do dołu, inne miejsce na napisy)
algos do osobnych plikow i pol dnia z dostosowywwaniem ich
"""


# main file, responsible for visualizing algos defined in other files

import random
import pygame

import os
import sys

# main window size and fill 
screen = pygame.display.set_mode((1110, 650)) #jak to sie ma do późniejszyc zmiennych width i length
screen.fill((255, 255, 255))

# title and icon settings
pygame.display.set_caption("Sorting Alogs")

# setting up a relative path for the icon
base_path = os.path.dirname(__file__)
icon_path = os.path.join(base_path, "icon.png")
img = pygame.image.load(icon_path)

pygame.display.set_icon(img)

# sorting window size
WIDTH = 900
LENGTH = 600   #brak późniejszych odwołań, zamienić
records = 186 # defining number of records to be sorted
array = [0]*records
arr_clr = [(0, 204, 102)]*records
clr = [(0, 204, 102), (255, 0, 0), (0, 0, 153), (255, 102, 0)] # recor

pygame.font.init()  # initializing text, so that it can be shown within the app
fnt = pygame.font.SysFont("calibri", 20)
fnt1 = pygame.font.SysFont("calibri", 15)

# generating array
def generate_arr():
    for i in range(1, records):
        arr_clr[i] = clr[0]
        array[i] = random.randrange(1, 100) # randomly generates hight of each record 

generate_arr()

def refill():
    screen.fill((255, 255, 255))
    draw()
    pygame.display.update()
    pygame.time.delay(7)

def check_events(): # Check if a window closing request was made                ### do zdefinionwania analogicznego jak w visualizerze, na poziomie algo   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

# Sorting Algo:Merge sort
def mergesort(array, left, right):
    mid = (left + right)//2
    if left < right:
        mergesort(array, left, mid)
        mergesort(array, mid + 1, right)
        merge(array, left, mid, mid + 1, right)
def merge(array, x1, y1, x2, y2):
    i = x1
    j = x2
    temp = []
    pygame.event.pump()
    while i <= y1 and j <= y2:
        arr_clr[i] = clr[1]
        arr_clr[j] = clr[1]
        refill()
        arr_clr[i] = clr[0]
        arr_clr[j] = clr[0]
        if array[i] < array[j]:
            temp.append(array[i])
            i += 1
        else:
            temp.append(array[j])
            j += 1
    while i <= y1:
        arr_clr[i] = clr[1]
        refill()
        arr_clr[i] = clr[0]
        temp.append(array[i])
        i += 1
    while j <= y2:
        arr_clr[j] = clr[1]
        refill()
        arr_clr[j] = clr[0]
        temp.append(array[j])
        j += 1
    j = 0
    for i in range(x1, y2 + 1):
        pygame.event.pump()
        array[i] = temp[j]
        j += 1
        arr_clr[i] = clr[2]
        refill()
        if y2-x1 == len(array)-2:
            arr_clr[i] = clr[3]
        else:
            arr_clr[i] = clr[0]

# Draw the array values
def draw():
    # Text should be rendered
    txt = fnt.render("PRESS ENTER TO START SORTING.", 1, (0, 0, 0))
    # Position where text is placed
    screen.blit(txt, (20, 20))
    txt1 = fnt.render("PRESS 'W' FOR A NEW ARRAY.", 1, (0, 0, 0))
    screen.blit(txt1, (20, 40))
    txt2 = fnt1.render("ALGORITHM USED: MERGE SORT", 1, (0, 0, 0))
    screen.blit(txt2, (600, 60))
    element_width = (WIDTH-150)//150
    boundry_arr = 900 / 150
    boundry_grp = 550 / 100
    pygame.draw.line(screen, (0, 0, 0), (0, 95), (900, 95), 6)
    for i in range(1, 100):
        pygame.draw.line(screen, (224, 224, 224), (0, boundry_grp * i + 100), (900, boundry_grp * i + 100), 1)

    # Drawing the array values as lines
    for i in range(1, records):
        pygame.draw.line(screen, arr_clr[i], (boundry_arr * i-3, 100), (boundry_arr * i-3, array[i]*boundry_grp + 100), element_width)

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
                mergesort(array, 1, len(array)-1)            #KLUCZOWE DLA DEFINICJI ALGOS
        draw()
        pygame.display.update()

pygame.quit()
