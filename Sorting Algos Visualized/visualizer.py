import SortingAlgos
import time
import os
import sys
import pygame

 # Set the window length and breadth  (Make sure that the breadth is equal to size of array. [512])
dimensions = (1024, 512)
# List all the algorithms available in the project in dictionary and call the necessary functions from algorithms.py
SortingAlgos = {"SelectionSort": SortingAlgos.SelectionSort(), "BubbleSort": SortingAlgos.BubbleSort(), "InsertionSort": SortingAlgos.InsertionSort(), "MergeSort": SortingAlgos.MergeSort(), "QuickSort": SortingAlgos.QuickSort()}
 
# Set the dimensions of the window and display it
display = pygame.display.set_mode(dimensions)
# Fill the window with purple hue
display.fill(pygame.Color("#a48be0"))

def check_events(): # Check if the pygame window was quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

def update(algorithm, swap1=None, swap2=None, display=display): # The function responsible for drawing the sorted array on each iteration
    display.fill(pygame.Color("#a48be0"))
    pygame.display.set_caption("Sorting Visualizer     Algorithm: {}     Time: {:.3f}      Status: Sorting...".format(algorithm.name, time.time() - algorithm.start_time)) # Display on title bar
    k = int(dimensions[0]/len(algorithm.array))
    for i in range(len(algorithm.array)):
        colour = (80, 0, 255)
        if swap1 == algorithm.array[i]:
            colour = (0,255,0)
        elif swap2 == algorithm.array[i]:
            colour = (255,0,0)
        # The most important step that renders the rectangles to the screen that gets sorted.
        # pygame.draw.rect(dsiplay_window, color_of_rectangle, size_of_rectangle)
        pygame.draw.rect(display, colour, (i*k,dimensions[1],k,-algorithm.array[i]))
    check_events()
    pygame.display.update()

def keep_open(algorithm, display, time): # Keep the window open until sort completion
    pygame.display.set_caption("Sorting Visualizer     Algorithm: {}     Time: {:.3f}      Status: Done!".format(algorithm.name, time))
    while True:
        check_events()


def main(args):
    # Case: user failed to choose an algorithm    
    if len(args) < 2:
        print("Please select a sorting algorithm.")
    # Case: user requests list of algorithms
    elif args[1] == "list":
            print("Available algorithms:\n\t" + "\n\t".join(SortingAlgos.keys()))
            sys.exit(0)
    # Case: user selected an algorithm
    else:
        try:
            algorithm = SortingAlgos[args[1]] # Collect algorithm
            _, time_elapsed = algorithm.run() # Run algorithm and time it
            keep_open(algorithm, display, time_elapsed) # Display results
        except:
            print("Error.")

if __name__ == "__main__":
    sys.argv.append("BubbleSort")
    main(sys.argv)