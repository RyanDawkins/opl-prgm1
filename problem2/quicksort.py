# Ryan Dawkins
# October 9th, 2014
# Programming Assignment 1

import random

# Class to deal with quicksort
class QuickSort(object):

    # This method does the recursive stradegy of quick sort
    def recursive(self, arr, left, right):

        # The array is sorted if this is false
        if  left < right:
            pivot = self.partition(arr, left, right)
            self.recursive(arr, left, pivot-1)
            self.recursive(arr, pivot+1, right)

    # Here is the iterative approach to quicksort using a stack
    def iterative(self, arr, left, right):

        stack = []
        top = -1

        stack.append(left)
        stack.append(right)
        top += 2

        # Runs while the stack is not empty
        while top >= 0:
            h = stack.pop()
            l = stack.pop()
            top -= 2
            p = self.partition(arr, l, h)

            # Checks if the pivot is greater than the left
            if p-1 > l:
                stack.append(l)
                stack.append(p-1)
                top += 2

            # Checks if the pivot is greater than the right
            if p+1 < h:
                stack.append(p+1)
                stack.append(h)
                top += 2


    # Method to return a new index
    def partition(self, arr, left, right):

        # getting our pivot value
        pivot = random.randint(left, right)
        pivotValue = arr[pivot]

        # swapping our pivot and the right
        arr[pivot], arr[right] = arr[right], arr[pivot]

        storeIndex = left
        for i in range(left, right):
            if arr[i] < pivotValue:
                arr[i], arr[storeIndex] = arr[storeIndex], arr[i]
                storeIndex += 1
        arr[storeIndex], arr[right] = arr[right], arr[storeIndex]
        return storeIndex
