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

from abc import ABCMeta, abstractmethod

import random
import pygame


# List all the algorithms available in the project in dictionary and call the necessary functions
# ALGOS = {
#         "BubbleSort": comparison_based_algos.BubbleSort(),
#         "MergeSort": comparison_based_algos.MergeSort(),    #działa ale cos nie wyswietla
#         "QuickSort": comparison_based_algos.QuickSort(),
#         "SelectionSort": comparison_based_algos.SelectionSort(),
#         "InsertionSort": comparison_based_algos.InsertionSort(),
#         "ShellSort": comparison_based_algos.ShellSort(),
#         #"HeapSort": comparison_based_algos.HeapSort()
#         #"RadixSort": non_comparison_based_algos.RadixSort(),
#         #"CountSort": non_comparison_based_algos.CountSort(),
#         #"BucketSort": non_comparison_based_algos.BuckerSort()
#         }

# main window size and fill
WIDTH = 1000
HEIGHT = 620

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
SCREEN.fill((255, 255, 255))

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
FNT1 = pygame.font.SysFont("calibri", 18)   # text for the instructions
FNT2 = pygame.font.SysFont("calibri", 25)   # text for displaying sorting properties


# generating array
def generate_arr():
    for i in range(1, RECORDS):
        ARR_COLOR[i] = COLOR[0]                 # defining array color within pre-defined palette
        ARRAY[i] = random.randrange(1, 100) # randomly generating height of each record

generate_arr()

def refill():
    SCREEN.fill((255, 255, 255))
    draw()
    pygame.display.update()
    pygame.time.delay(8)                    # setting number of milliseconds in which each operation is being done

def check_events():                         # checking if window closing request was made
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

class Algorithm(metaclass=ABCMeta):
    '''universal algorithm class'''
    def __init__(self, name):
        self.array = random.sample(range(512), 512) # Random array of size 512
        self.name = name # Get name of the variable

    def update_display(self, swap1=None, swap2=None):
        import visualizer
        visualizer.update(self, swap1, swap2) #pass the indexes to be swapped into the visualizer

    def run(self):
        '''start the timer and run the algorithm'''
        self.start_time = time.time()
        self.algorithm()
        time_elapsed = time.time() - self.start_time
        return self.array, time_elapsed

    @abstractmethod
    def algorithm(self):
        raise TypeError(f"Algorithm.algorithm() has not been overwritten.")




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
    txt1 = FNT1.render("Press 'Enter' to start sorting.", 1, (0, 0, 0))    # rendering the text
    SCREEN.blit(txt1, (680, 50))                                        # setting its position

    txt2 = FNT1.render("Press 'W' for a new array.", 1, (0, 0, 0))
    SCREEN.blit(txt2, (680, 80))

    txt3 = FNT1.render("Press 'A' to choose a different algorithm.", 1, (0, 0, 0))
    SCREEN.blit(txt3, (680, 110))

    txt4 = FNT2.render("Algorithm used: Merge Sort", 1, (0, 0, 0))
    SCREEN.blit(txt4, (680, 250))

#    txt5 = FNT2.render("Time passed: {:.2f}".format(time.time() - algorithm.start_time), 1, (0, 0, 0))                #OPISZ CZAS !!!!!!!!!!!!!!!!!!
#    SCREEN.blit(txt5, (680, 300))


    record_width = 6                                                   # width of a single record
    space_btwn_rec = 7                                                 # space between records
    height_rec = 6.5                                                   # height of a single record

    # drawing the array values as lines
    for i in range(1, RECORDS):
        pygame.gfxdraw.line(SCREEN, ARR_COLOR[i], (0, space_btwn_rec * i-3), (ARRAY[i]*height_rec, space_btwn_rec * i-3), record_width)
      # pygame.draw.line syntax: line(surface, color, start_pos, end_pos, width)

# boolean variable to run the program in while loop
RUNNING = True

# main loop
while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # setting up a possibility to quit while not running
            RUNNING = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                generate_arr()
            # if event.key == pygame.K_a:
            #     ponowny wybór algo
            if event.key == pygame.K_RETURN:
                mergesort(ARRAY, 1, len(ARRAY)-1)            #KLUCZOWE DLA DEFINICJI ALGOS
        draw()
        pygame.display.update()

pygame.quit()