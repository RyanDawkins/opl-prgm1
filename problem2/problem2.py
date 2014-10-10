# Ryan Dawkins
# October 9th, 2014
# Programming Assignment 1

from quicksort import QuickSort

if __name__ == "__main__":
    sorter = QuickSort()

    a0 = [200,133,41,34,2,11]
    a1 = a0[:] # Creates a copy of a0

    # Example showing the recursive method
    print "Recursive:"
    print a0
    sorter.recursive(a0, 0, len(a0)-1)
    print a0

    print

    # Example showing the iterative method
    print "Iterative:"
    print a1
    sorter.iterative(a1, 0, len(a1)-1)
    print a1
