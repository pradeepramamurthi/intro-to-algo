global heap_size

def build_max_heap(A):
    global heap_size
    heap_size = len(A) - 1

    n = len(A)
    for i in range((n // 2), -1, -1):
        max_heapify(A, i)
    return A


def max_heapify(A, i):
    global heap_size
    self = i
    lhs = (2 * self) + 1
    rhs = lhs + 1

    if lhs <= heap_size and A[lhs] > A[self]:
        largest = lhs
    else:
        largest = i
    if rhs <= heap_size and A[rhs] > A[largest]:
        largest = rhs
    if self != largest:
        A[self], A[largest] = A[largest], A[self]
        """cal max_heapify again after the swap to ensure the child node (& child tree) 
           after the insertion of the new value still confirms to the max heap invariant """
        max_heapify(A, largest)
    return A[0:heap_size + 1]


def max(A):
    # build_max_heap(A)
    return A[0]


def parent(i):
    if i == 0:
        return None
    """Usually i//2 for 1 index heaps, but adjusted for 0 index start"""
    return (i + 1) // 2 - 1


def reset_heap_size(A):
    global heap_size
    heap_size = len(A) - 1
    return heap_size


def extract_max(A):
    global heap_size
    reset_heap_size(A)

    maximum = A[0]
    A[0], A[len(A) - 1] = A[len(A) - 1], A[0]

    heap_size = heap_size - 1
    return maximum, max_heapify(A, 0)
    # return maximum


def insert(A, key):
    global heap_size
    reset_heap_size(A)

    """Append the new element to the end of the list"""
    A.append(key)

    """Now increase the heap size by 1"""
    heap_size = heap_size + 1
    """Get the index of the key you want to insert"""
    key_index = A.index(key)

    """Heapify to fix any violations going up till root only if there is a violation"""
    while key_index > 0 and A[parent(key_index)] < A[key_index]:
        A = max_heapify(A, parent(key_index))
        key_index = parent(key_index)

    return A


def delete(A, key):
    global heap_size
    reset_heap_size(A)
    reset_heap_size(A)
    """Get the index of the key you want to delete"""
    key_index = A.index(key)
    """swap it with the last element"""
    A[key_index], A[len(A) - 1] = A[len(A) - 1], A[key_index]
    """decrease the heap size by 1 """
    heap_size = heap_size - 1
    return max_heapify(A, 0)


def check_invariant(A):
    heap_size = len(A) - 1
    mid = heap_size // 2

    for i in range(mid, -1, -1):
        lhs = (2 * i) + 1
        rhs = lhs + 1
        if lhs <= heap_size and A[lhs] > A[i]:
            largest = lhs
        else:
            largest = i
        if rhs <= heap_size and A[rhs] > A[largest]:
            largest = rhs
        if i != largest:
            return False
            break
        else:
            continue
    return True


def driver():
    A = [16, 14, 0, 18, 9, 1]

    print("Array before building max heap: ")
    print(A)

    print("**** built_max_heap ****")
    built_max_heap = build_max_heap(A.copy())

    print(built_max_heap)
    print()

    print("Max of built_max_heap: ")
    print(max(built_max_heap))
    print()

    print("Extract Max of built_max_heap")
    print(extract_max(built_max_heap.copy()))
    print()

    print("built_max_heap After deletion of a key ")
    print(delete(built_max_heap.copy(), 14))
    print()

    print("built_max_heap After insertion of a key ")
    print(insert(built_max_heap.copy(), 1450))

    # print(check_invariant(built_max_heap.copy()))
    # print(check_invariant(extract_max(built_max_heap.copy())[1]))
    # print(check_invariant(delete(built_max_heap.copy(), 14)))
    # print(check_invariant(insert(built_max_heap.copy(), 1450)))


if __name__ == "__main__":
    driver()
