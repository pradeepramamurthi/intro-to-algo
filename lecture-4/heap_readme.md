A Heap is a data structure that implements the ADT Priority Queue

An implementation of  priority queue ADT should support the following operations:

insert(S,x): insert an element x in priority queue S (Where S is a set of elements)
max(S): returns the element of the queue which has the largest key.
extract_max(S): returns element of S with the largest key and then removes that element from S.
increase_key(S,x,k): increase the value of element x's key to new value k. (Where k >= x)

Heap (max or min) is a concrete implementation of the ADT priority queue.
It supports the following operations:

build_max_heap: produce a max-heap from an unordered Array
max_heapify: Correct a single violation of the Heap's invariant property in a subtree at its root.

Other operations are insert, extract_max, heapsort.

Max Heap's invariant: The key of a node >= the key of it's child nodes.

A Heap is an Array can be visualised as a binary Tree.

root of the tree = first element of the Array corresponding to i.
parent(i) = i/2 Returns the node(i)'s parent index.
left(i) = 2i: Returns the index of the node(i)'s left child.
right(i) = 2i + 1: Returns the index of node(i)'s right child.

Height of a Binary Tree = O(log n)

Build_Max_Heap(A)
=================
Converts A[1..n] to a max heap.

//Pseudocode
build_max_heap(A):
    for i=n/2 to 1:
        do max_heapify(A, i)

why start at n/2? Because all elements after that i.e. A[n/2+1 ..n] are leaf nodes.
(as 2i is > n for all i >= n/2+1)

Time Complexity to build max heap: O(n)

Max_heapify
============

Assume that the trees rooted at left(i) and right(i) are max-heaps.
If an element A[i] violates the max-heap invariant property, then correct the violation
by moving element A[i] down the Binary Tree - ensuring that the invariant property holds good.
Time complexity of Max_heapify is O(log n)

//Pseudocode
"""where i is the node you want o heapify"""
max_heapify(A,i):
    l= left(i)
    r = right(i)
    if (l <= heap-size(A) and A[l] > A[i]):
        largest = l
    else:
        largest = i
    if (r <= heap-size(A) and A[r] > A[largest]):
        largest = r
    if largest <> i:
        then swap A[i] with A[largest]
        max_heapify(A, largest)
    
Heap-Sort
=========
1. Create Max Heap from unordered array
2. Find max element. It will be at A[1]
3. Now Swap A[1] and A[n] where A[n] is the last element.
   Now max element is at the end of the heap & array.
4. Discard the node n from the Heap by decrement heap size by 1.
5. As new root may violate max heap's invariant ,  call max_heapify to fix any violations.
6. Go to step2 unless the heap is empty.
7. The array is the sorted in ascending order.
   If you want the array sorted in descending order use min heap in the same manner.

Run Time of Heap Sort:
After n iterations the heap is empty.
every iteration involves a swap and a max_heapify (c + O(log n))

Total time for Heap sort : O(n log n)
