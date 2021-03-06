"""
ZROZUMIEC MECHANIZM KOLOROWANIA NA WOLNIEJSZYM TEMPIE
POTEM PRZEMODELOWAC TYLKO MERGE SORT
potem timer
potem 'sorting...' i ze done! jak skonczy
potem załadowac inne algorytmy
przy wybieraniu powinno sie wyswietlac tak jak w excelu komentarze, ze ten najszybszy ten taki

https://www.youtube.com/watch?v=r7Dtus7N4pI
zrozumiec dekoratory (naprawde), bo ta metaclasa jest do ogarniecia

nie powinna moc sie sortowac juz raz posortowana zbiorowosc
zmiana algorytmu nie powinna wywoływac zmiany tabeli do sortowania,  bo nie ma porownowalnosci
"""
# main file, responsible for visualizing algos defined in other files

import os
import sys
import time
import subprocess

import random
import pygame

import choose_algo
import algos_defined


# dict containing all the algorithms available in the project with the necessary functions
ALGOS = {
        "Bubble Sort": algos_defined.BubbleSort(),
        "Merge Sort": algos_defined.MergeSort(),
        "Quick Sort": algos_defined.QuickSort(),
        "Selection Sort": algos_defined.SelectionSort(),
        "Insertion Sort": algos_defined.InsertionSort(),
        "Shell Sort": algos_defined.ShellSort(),
        #"Heap Sort": algos_defined.HeapSort()
        #"Radix Sort": algos_defined.RadixSort(),
        #"Count Sort": algos_defined.CountSort(),
        #"Bucket Sort": algos_defined.BucketSort()
        }

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
COLOR = [(0, 0, 255), (255, 255, 0), (255, 0, 0), (5, 124, 0)] # color palette [blue, yello, red, dark green]

pygame.font.init()                          # initializing text, so that it can be shown within the app
FNT1 = pygame.font.SysFont("arial", 18)   # text for the instructions
FNT2 = pygame.font.SysFont("arial", 25)   # text for displaying sorting properties


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
    pygame.time.delay(700)                    #7  setting number of milliseconds in which each operation is being done

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
    #tu jakis warunek, tak zeby enter zmienial sie na sorting.. i na done...
    txt1 = FNT1.render("Press 'Enter' to start sorting.", 1, (0, 0, 0))    # rendering the text
    SCREEN.blit(txt1, (680, 450))                                        # setting its position
    txt2 = FNT1.render("Press 'S' for a new array.", 1, (0, 0, 0))
    SCREEN.blit(txt2, (680, 480))
    txt3 = FNT1.render("Press 'A' to choose a different algorithm.", 1, (0, 0, 0))
    SCREEN.blit(txt3, (680, 510))
    txt4 = FNT2.render("Algorithm: {}".format(choose_algo.dropdown), 1, (0, 0, 0))
    SCREEN.blit(txt4, (680, 50))
    txt5 = FNT2.render("Time passed: {:.2f} seconds".format(time.time()), 1, (0, 0, 0))    # time.time() - algorithm.start_time
    SCREEN.blit(txt5, (680, 100))

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
    SCREEN.fill((255, 255, 255))        # refreshing the background; solves the problem of the old array not being completely removed and antialiasing of the font
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # possibility to quit while not running
            RUNNING = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                generate_arr()
            if event.key == pygame.K_a: # possibility to re-run the program with a different algo
                pygame.quit()
                subprocess.call(["python", os.path.join(sys.path[0], __file__)] + sys.argv[1:])
            if event.key == pygame.K_RETURN:
                algorithm = ALGOS.get(choose_algo.dropdown)
                _, time_elapsed = algorithm.run()
        draw()
        pygame.display.update()

pygame.quit()
