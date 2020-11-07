"""
ogarnij dodaj timer
ze 'sorting' i ze done! jak skonczy
* załadowac inne algorytmy

ROZWALA SIE JAK SIE GENERUJE NOWA array!!!


antialiasing na tych napisach przed uruchomieniem ogarnac bo to zle wyglada

dodać czas i napis "done!"
algos do osobnych plikow i pol dnia z dostosowywwaniem ich

jak jest posortowane to nie powinno byc mozna jeszcze raz sortowac posortowanej tabeli
jak po posortowaniu naciskasz W (zeby wygenerowac nowa tebale, to widac stare sortowanie_)
"""


# main file, responsible for visualizing algos defined in other files

import os
import sys
import time
import subprocess

from abc import ABCMeta, abstractmethod

import random
import pygame

import choose_algo
import comparison_based_algos
import non_comparison_based_algos




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
#         #"BucketSort": non_comparison_based_algos.BucketSort()
#         }

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



# main window size and fill
WIDTH = 1000
HEIGHT = 620

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
SCREEN.fill((255, 255, 255))                # defining white background

# title and icon settings
pygame.display.set_caption("Sorting Alogs")

# setting up a relative path for the icon
BASE_PATH = os.path.dirname(__file__)
ICON_PATH = os.path.join(BASE_PATH, "icon.png")
IMG = pygame.image.load(ICON_PATH)

pygame.display.set_icon(IMG)

RECORDS = 89                                # defining number of RECORDS to be sorted
DEFAULT_REC = [(0, 0, 0)]*RECORDS           # default record, to be modified/colored as the algo is running
ARRAY = [0]*RECORDS                         # pre-defining the array as a list of x RECORDS with height of 0
COLOR = [(46, 63, 222), (255, 255, 8), (255, 0, 0), (97, 223, 0)] # color palette [blue, yellow, red, green]

pygame.font.init()                          # initializing text, so that it can be shown within the app
FNT1 = pygame.font.SysFont("calibri", 18)   # text for the instructions
FNT2 = pygame.font.SysFont("calibri", 25)   # text for displaying sorting properties


# generating array
def generate_arr():
    for i in range(1, RECORDS):
        DEFAULT_REC[i] = COLOR[0]             # defining array color within pre-defined palette
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

# Sorting Algo:Merge sort
def mergesort(ARRAY, left, right):
    mid = (left + right)//2
    if left < right:
        mergesort(ARRAY, left, mid)
        mergesort(ARRAY, mid + 1, right)
        algorithm(ARRAY, left, mid, mid + 1, right)
def algorithm(ARRAY, x1, y1, x2, y2):
    i = x1
    j = x2
    temp = []
    pygame.event.pump()
    while i <= y1 and j <= y2:
        DEFAULT_REC[i] = COLOR[1]
        DEFAULT_REC[j] = COLOR[1]
        refill()
        DEFAULT_REC[i] = COLOR[0]
        DEFAULT_REC[j] = COLOR[0]
        if ARRAY[i] < ARRAY[j]:
            temp.append(ARRAY[i])
            i += 1
        else:
            temp.append(ARRAY[j])
            j += 1
    while i <= y1:
        DEFAULT_REC[i] = COLOR[1]
        refill()
        DEFAULT_REC[i] = COLOR[0]
        temp.append(ARRAY[i])
        i += 1
    while j <= y2:
        DEFAULT_REC[j] = COLOR[1]
        refill()
        DEFAULT_REC[j] = COLOR[0]
        temp.append(ARRAY[j])
        j += 1
    j = 0
    for i in range(x1, y2 + 1):
        pygame.event.pump()
        ARRAY[i] = temp[j]
        j += 1
        DEFAULT_REC[i] = COLOR[2]
        refill()
        if y2-x1 == len(ARRAY)-2:
            DEFAULT_REC[i] = COLOR[3]
        else:
            DEFAULT_REC[i] = COLOR[0]


def draw():
    txt1 = FNT1.render("Press 'Enter' to start sorting.", 1, (0, 0, 0))    # rendering the text
    SCREEN.blit(txt1, (680, 50))                                        # setting its position
    txt2 = FNT1.render("Press 'W' for a new array.", 1, (0, 0, 0))
    SCREEN.blit(txt2, (680, 80))
    txt3 = FNT1.render("Press 'A' to choose a different algorithm.", 1, (0, 0, 0))
    SCREEN.blit(txt3, (680, 110))
    txt4 = FNT2.render("Algorithm used: {}".format(choose_algo.dropdown), 1, (0, 0, 0))
    SCREEN.blit(txt4, (680, 250))
    # txt5 = FNT2.render("Time passed: {:.2f}".format(time.time() - algorithm.start_time), 1, (0, 0, 0))                #OPISZ CZAS !!!!!!!!!!!!!!!!!!
    # SCREEN.blit(txt5, (680, 300))

    record_width = 6                                                   # width of a single record
    space_btwn_rec = 7                                                 # space between records
    height_rec = 6.5                                                   # height of a single record

    check_events()                                                     # setting up a possibility to quit while running

    # drawing the array values as lines
    for i in range(1, RECORDS):
        pygame.draw.line(SCREEN, DEFAULT_REC[i], (0, space_btwn_rec * i-3), (ARRAY[i]*height_rec, space_btwn_rec * i-3), record_width)
      # pygame.draw.line syntax: line(surface, color, start_pos, end_pos, width)

# boolean variable to run the program in while loop
RUNNING = True

# main loop
while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # possibility to quit while not running
            RUNNING = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                generate_arr()
            if event.key == pygame.K_a: # possibility to re-run the program with a different algo
                pygame.quit()
                subprocess.call(["python", os.path.join(sys.path[0], __file__)] + sys.argv[1:])
            if event.key == pygame.K_RETURN:
                mergesort(ARRAY, 1, len(ARRAY)-1)            #KLUCZOWE DLA DEFINICJI ALGOS
        draw()
        pygame.display.update()

pygame.quit()
