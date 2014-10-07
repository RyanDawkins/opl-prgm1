import random

class QuickSort(object):

    def quicksort(self, A, i, k):
        raise NotImplementedError( "Should have implemented this" )

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
