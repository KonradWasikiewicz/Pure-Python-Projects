"""

https://www.geeksforgeeks.org/analysis-of-different-sorting-techniques/
https://www.tutorialspoint.com/python_data_structure/python_sorting_algorithms.htm
https://medium.com/towards-artificial-intelligence/visualize-interesting-sorting-algorithms-with-python-bdd64bdd0713
https://dev.to/kgprajwal/build-a-sorting-visualizer-in-python-2oej


Comparison based sorts:
bubble, insertion, quick, selection, merge, heap

Non-comparison based sorts:

radix, count, bucket 

"""
import random
import matplotlib.pyplot as plt
import matplotlib.animation as anim


#miejsce na import i zmienne globalen

class Algorithm:
    def __init__(self, name):
        self.array = random.sample(range(512), 512) # Random array of size 512
        self.name = name # Get name of the variable

    def update_display(self, swap1=None, swap2=None):                                                           # TO TRZEBA ZMIENIC 
        import visualizer
        visualizer.update(self, swap1, swap2) # pass the indexes to be swapped into the visualizer

    def run(self): # Start the timer and run the algorithm
        self.start_time = time.time() 
        self.algorithm()
        time_elapsed = time.time() - self.start_time
        return self.array, time_elapsed




'''Bubble sort - each pair of adjecent elements in a list is compared and elements are swapped if not in order'''

class BubbleSort(Algorithm):
    def __init__(self):
        super().__init__("BubbleSort")

    def algorithm(self):
        for i in range(len(self.array)):
            for j in range(len(self.array)-1):
                if self.array[j] > self[j+1]:
                    self.array[j], self.array[j+1] = self.array[j+1], self.array[j]
                    
