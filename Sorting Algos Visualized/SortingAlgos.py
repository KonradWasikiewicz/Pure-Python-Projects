"""

https://www.geeksforgeeks.org/analysis-of-different-sorting-techniques/
https://www.tutorialspoint.com/python_data_structure/python_sorting_algorithms.htm
https://dev.to/kgprajwal/build-a-sorting-visualizer-in-python-2oej
 
 

Comparison based sorts:
bubble, insertion, quick, selection, merge, heap, shell 

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
        self.name = name #get name of the variable

    def update_display(self, swap1=None, swap2=None):                                                           # TO TRZEBA ZMIENIC 
        import visualizer
        visualizer.update(self, swap1, swap2) #pass the indexes to be swapped into the visualizer

    def run(self): #start the timer and run the algorithm
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
            for i in range(len(self.array) -1 -iteration): #as we know that the last element of each iteration is on its place, to optimize the algo we reduce range for i with each done iteration
                if self.array[i] > self.array[i+1]:
                    self.array[i], self.array[i+1] = self.array[i+1], self.array[i]  #elements swap takes place here
            self.update_display(self.array[i], self.array[i+1])

''' Merge sort - divide the array in half, sorts them and merges two sub-sorted arrays into one'''
class MergeSort(Algorithm):
    def __init__(self):
        super().__init__("MergeSort")

    def algorithm(self, array = []):           
        if array == []:
            array = self.array
        if len(self.array) > 1:
            middle = len(self.array) // 2
            left = self.array[:middle]
            right = self.array[middle:]
        #recurvise call on left and right, so that we end up with 1 element of right and left each (single pair)
            self.algorithm(left)
            self.algorithm(right)
        #iterators used for traversing each of the two lists
            i, j = 0, 0
        #iterator used to keep track of the result list 
            k = 0
        
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    #use the left value first 
                    self.array[k] = left[i]
                    #move the iterator to the next number
                    i += 1
                else:
                    #use the right value first
                    self.array[k] = right[j]
                    #move the iterator to the next number
                    j += 1 
                #next number on the main list
                k += 1 
            self.update_display()
            #the other value from the pair 
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

    def algorithm(self, array = [], start = 0, end = 0):
        if array == []:
            array = self.array
            end = len(array) - 1
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
            #if the current value we're looking at is larger than the pivot it's in the right place (right side of pivot) and we can move left,
            #to the next element. We also need to make sure we haven't passed the low point, since that indicates we have already moved all the elements to their correct side of the pivot
            while low <= high and array[high] >= pivot:
                high = high - 1
            #opposite process of the one above
            while low <= high and array[low] <= pivot:
                low = low + 1
            #we either found a value for both high and low that is out of order
            #or low is higher than high, in which case we exit the loop
            if low <= high:
                array[low], array[high] = array[high], array[low]
                #the loop continues
            else:
                #we exit out of the loop
                break
    
        array[start], array[high] = array[high], array[start]
        self.update_display(array[start], array[high])
        
        return high                                                                       # moze niepotrzebne?

'''Selection sort - finding minimum value in an array and swapping it with nth element 
(beginning at the first one), so that each time we iterate the analyzed array becomes shorter'''
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

'''Insertion sort - comparing element n with n-1 and if n-1 bigger than n, swapping it. 
    If not iterating through the list to the very beginning to place it correctly'''

class InsertionSort(Algorithm):
    def __init__(self):
        super().__init__("InsertionSort")

    def algorithm(self):
        for i in range(len(self.array)):
            nth_element = self.array[i]
            x = i-1
            while x >= 0 and self.array[x] > nth_element:
                self.array[x+1] = self.array[x]
                x -= 1
            self.array[x+1] = nth_element
            self.update_display(self.array[x], self.array[i])
            
'''Shell sort - take a second half of the array and compare every element with an element from the first half'''
class ShellSort(Algorithm):
    def __init__(self):
        super().__init__("ShellSort")

    def algorithm(self):
        gap = len(self.array) // 2 #cut the list in half
        while gap > 0:
            for i in range(gap, len(self.array)): #analyze the second half first
                temp = self.array[i] #value storage for the element that is being analyzed 
                j = i

                while j >= gap and self.array[j - gap] > temp: #compare the value with the corresponding element in the first half
                    self.array[j] = self.array[j - gap] #if number in the first half is bigger than number in the second half, replace the second half value 
                    self.update_display(self.array[j], self.array[j - gap]) #if it ain't bigger, iterate throught the first half to search for a smaller value 
                    j = j-gap
                self.array[j] = temp #place the smaller value in the first half (if first half value is larger, if not - do not replace anything)
                self.update_display(self.array[j], self.array[j - gap])
    # Reduce the gap for the next element

            gap = gap//2


'''Heap sort - based on heap data structure (maxheap). Exchanges the last element of the array with the root (first element) and goes down the tree to sort the elements. At the end root must be the biggest of all.   '''

class HeapSort(Algorithm):
    def __init__(self):
        super().__init__("HeapSort")

    def heap_it(array = [], arr_len, i):
        if array == []:
            array = self.array
        parent = i # point the parent element 
        left_node = 2*i + 1 # pre-defined formula for the left node 
        right_node = 2*i + 2 # pre-defined formula for the right node
        
        # checking if left child as defined above is a part of the array and is greater than root 
        if left_node < arr_len and self.array[i] < self.array[left_node]:
            parent = left_node # switch root for the bigger element (so that the tree is valid)
        # checking if right child as defined above is a part of the array and is greater than root 
        if right_node < arr_len and self.array[parent] < self.array[right_node]:
            parent = right_node # switch root for the bigger element (so that the tree is valid)
        # if parent has been modified, implement it into the array
        if parent != i:
            self.array[i], self.array[parent] = self.array[parent], self.array[i] 
            
            # recurisve function to move it further down the array
            heap_it(self.array, arr_len, parent)
            
    def algorithm(self):  
        last_pos_pointer = len(self.array)-1 # defines iteration boundary
        arr_len = len(self.array)
        
        for i in range(arr_len//2 -1, -1, -1):
            heap_it(self.array, arr_len, i)
            
        for i in range(last_pos_pointer,0,-1): # counting down the range
            self.array[i], self.array[0] = self.array[0], self.array[i] #swap
            heap_it(self.array, i, 0)