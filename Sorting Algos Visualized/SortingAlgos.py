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

    def algorithm(self, array = []):           
        if array = []:
            array = self.array
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
 
''' Quick sort - picks an elements as a pivot and sorts the given array around the pivot'''
class QuickSort(Algorithm):
    def __init__(self):
        super().__init__("QuickSort")

    def algorithm(self, array = [], start=0, end=len(array) - 1):
        if array = []:
            array = self.array
        if start >=  end:
            return 
        pivot = self.partition(array,start,end)
        self.algorithm(array,start,pivot-1)
        self.algorithm(array,pivot+1,end)

    def partition(self, array, start, end):
        pivot = array[start]
        low = start+1
        high = end
    
        while True:
            #If the current value we're looking at is larger than the pivot it's in the right place (right side of pivot) and we can move left,
            #to the next element. We also need to make sure we haven't passed the low point, since that indicates we have already moved all the elements to their correct side of the pivot
            while low <= high and array[high] >= pivot:
                high = high - 1
            # Opposite process of the one above
            while low <= high and array[low] <= pivot:
                low = low + 1
            # We either found a value for both high and low that is out of order
            # or low is higher than high, in which case we exit the loop
            if low <= high:
                array[low], array[high] = array[high], array[low]
                # The loop continues
            else:
                # We exit out of the loop
                break
    
        array[start], array[high] = array[high], array[start]
        self.update_display(array[start], array[high])
        
        return high                                                                       # moze niepotrzebne?

'''Selection sort - finding minimum value in an array and swapping it with nth element, so that each time we iterate the analyzed array becomes shorter'''
class SelectionSort(Algorithm):
    def __init__(self):
        super().__init__("SelectionSort")

    def algorithm(self):
        for i in range(len(self.array)):
            min_id = i
            for j in range(i+1, len(self.array)):
                if self.array[j] < self.array[min_id]:
                    min_id = j
            self.array[i], self.array[min_id] = self.array[min_id], self.array[i]
            self.update_display(self.array[i], self.array[min_id])