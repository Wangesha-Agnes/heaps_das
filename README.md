# HEAP DATA STRUCTURE

A heap is a data structure that is a complete binary tree and satisfies the heap property where for every node the value of its children is less than or equal to its own value.

HEAP PROPERTIES
1. Heaps are implemented in an array.
2. Parent node in Max-heap tree has a larger value than its children nodes.
3. Parent node in min-heap tree has a value smaller than its children nodes.
4. All levels in a heap should be full.

ADVANTAGES
1. Efficient insertion and deletion.
2. Efficient priority queue.
3. Guaranteed access to the minimum and maximum element.
4. Space efficiency.

DISADVANTAGES
1. Lack of flexibility.
2. Not ideal for searching.
3. Not a stable data structure.
4. Each level  of the tree has at most two children, a left child and a right child.
5. Heap property min heap:less or equal to values of children, max heap:greater or equal to the values of children.

APPLICATION OF BINARY TREE
1. Search for a specific element using the structure of binary trees.
2. Can be used to implement file systems each node represents a directory or file.
3. Stores data in database systems with each node representing a record.

INSERTION
1. Increase the heap size by one to ensure there is space to store a new element.
2. Insert the new element at the end of the heap.
3. The newly inserted element might disrupt the heap properties either min heap or max heap.
4. To restore the properties we perform a bottom-up heapify operation which compares the newly inserted element with its parent and swap if necessary to maintain the heap property.
5. Repeat the process until the element reaches its correct position in the heap.

DELETION
1. Replace the element to be deleted by the last element.
2. Delete the last element from the heap .
3. Check if the now placed element follows the heap property  if so leave it if not heapify the last node placed at the position of root.

