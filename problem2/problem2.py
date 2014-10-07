from quicksortrecursive import QuickSortRecursive

if __name__ == "__main__":
    sorter = QuickSortRecursive()
    a = [1, 0, 2, 4]
    print a
    sorter.quicksort(a, 0, len(a)-1)
    print a
