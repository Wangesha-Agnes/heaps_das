# HEAP DATA STRUCTURE
WHAT IS A HEAP
A heap is a data structure that is a complete binary tree and satisfies the heap property where for every node the value of its children is less than or equal to its own value.
HEAP PROPERTIES
Heaps are implemented in an array.
Parent node in Max-heap tree has a larger value than its children nodes.
Parent node in min-heap tree has a value smaller than its children nodes.
All levels in a heap should be full.

ADVANTAGES
Efficient insertion and deletion.
Efficient priority queue.
Guaranteed access to the minimum and maximum element.
Space efficiency.

DISADVANTAGES
Lack of flexibility.
Not ideal for searching.
Not a stable data structure.
Each level  of the tree has at most two children, a left child and a right child.
Heap property min heap:less or equal to values of children, max heap:greater or equal to the values of children.
Applications of binary tree.
Search for a specific element using the structure of binary trees.
Can be used to implement file systems each node represents a directory or file.
Stores data in database systems with each node representing a record.

INSERTION
Increase the heap size by one to ensure there is space to store a new element.
Insert the new element at the end of the heap.
The newly inserted element might disrupt the heap properties either min heap or max heap.
To restore the properties we perform a bottom-up heapify operation which compares the newly inserted element with its parent and swap if necessary to maintain the heap property.
Repeat the process until the element reaches its correct position in the heap.

DELETION
Replace the element to be deleted by the last element.
Delete the last element from the heap .
Check if the now placed element follows the heap property  if so leave it if not heapify the last node placed at the position of root.

