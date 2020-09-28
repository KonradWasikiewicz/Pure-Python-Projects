"""

https://www.geeksforgeeks.org/analysis-of-different-sorting-techniques/
https://www.tutorialspoint.com/python_data_structure/python_sorting_algorithms.htm
https://medium.com/towards-artificial-intelligence/visualize-interesting-sorting-algorithms-with-python-bdd64bdd0713
https://dev.to/kgprajwal/build-a-sorting-visualizer-in-python-2oej
https://www.educative.io/edpresso/merge-sort-in-python

Comparison based sorts:
bubble, insertion, quick, selection, merge, heap

Non-comparison based sorts:

radix, count, bucket 

"""
import random
import matplotlib.pyplot as plt
import matplotlib.animation as anim   #chyba niekoniecznie jak bedzie oddzielny plik na visualizer 


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
        for iteration in range(len(self.array)):   
            for i in range(len(self.array) -1 -iteration): # as we know that the last element of each iteration is on its place, to optimize the algo we reduce range for i with each done iteration
                if self.array[i] > self.array[i+1]:
                    self.array[i], self.array[i+1] = self.array[i+1], self.array[i]  # elements swap takes place here
            self.update_display(self.array[i], self.array[i+1])

''' Merge sort - divide the array in half, sorts them and merges two sub-sorted arrays into one'''
class MergeSort(Algorithm):
    def __init__(self):
        super().__init__("MergeSort")

    def algorithm(self):           
        if len(self.array) > 1:
            middle = len(self.array) // 2
            left = self.array[:middle]
            right = self.array[middle:]
        # recurvise call on left and right, so that we end up with 1 element of right and left each (single pair)
            algorithm(left)
            algorithm(right)
        # iterators used for traversing each of the two lists
            i, j = 0, 0
        # iterator used to keep track of the result list 
            k = 0
        
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    # use the left value first 
                    self.array[k] = left[i]
                    # move the iterator to the next number
                    i += 1
                else:
                    # use the right value first
                    self.array[k] = right[j]
                    # move the iterator to the next number
                    j += 1 
                # next number on the main list
                k += 1 
            self.update_display()
            # the other value from the pair 
            while i < len(left):
                self.array[k] = left[i]
                i += 1
                k += 1 
            while j < len(right):
                self.array[k] = right[j]
                j += 1
                k += 1 
            self.update_display()
