from quicksort import QuickSort

if __name__ == "__main__":
    sorter = QuickSort()
    a = [1, 0, 2, 4]
    print a
    sorter.iterative(a, 0, len(a)-1)
    print a
