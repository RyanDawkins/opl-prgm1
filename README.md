#OPL Program 1
* For viewing it is recommended to go to https://github.com/RyanDawkins/opl-prgm1
* This file will discuss all three problems. Our programs are written in the
  python programming language. To run our programs you simply type:
  ```sh
  python program.py
  ```

##Problem 1
### Overview
There are multiple layers of abstraction that happen in this program.
For example, we have a class called Storage which is essentially an interface
to force the implementation of certain methods such as store, delete, list.
Those are the commands that are abstracted into different classes.

The two main classes that implement the main of the program using structs
to store the data versus arrays is in the ArrayConsole and the StructConsole.

You can test this by running problem1.py

##Problem 2
### Overview
There is one class QuickSort for this problem. They both use the same partition
method. Running the class is easy, simply create a new QuickSort object
and then run either ```Quicksort.recursive()``` or ```QuickSort.iterative()```. You can
test this by running problem2.py
