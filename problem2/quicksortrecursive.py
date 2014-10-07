from quicksort import QuickSort

class QuickSortRecursive(QuickSort):
    
    def quicksort(self, A, i, k):
        if  i < k:
            p = self.partition(A, i, k)
            self.quicksort(A, i, p-1)
            self.quicksort(A, p+1, k)
