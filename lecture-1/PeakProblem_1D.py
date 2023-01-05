"""Given an array A with n elements, find any peak element A[i] where A[i] ≥ A[i − 1]
and A[i] ≥ A[i + 1]. For elements on the boundaries of the array, the element only needs to be
greater than or equal to its lone neighbor to be considered a peak."""

"""
Algo Logic:
1. Find the n/2 element
2. If n/2 element is >= (n/2)-1 and >= (n/2)+1 then return n/2 (It is the peak)
3. if n/2 element is < (n/2) -1 then use logic in steps 1 & 2 on the LHS array i.e Array[0] to Array[(n/2)] recursively.
4. If step 3 does not give a peak element then use Array[n/2] + 1 to Array[len(Array)] + 1 recursively.
5. Edge case: Check if the element is start/end of array. If start/end & >= it's only neighbour return that element as the peak.
6. The above logic is run in Time Complexity of O(log n).
   T(n) = T(n/2) :Running time of half of the input value + O(1) : Constant time to Compare to neighbours
   On every pass: T(n/2) + O(1) + T(n/4) + O(1) + T(n/8) + O(1).... is repeated till only one element is left = O(log n)
"""


def find_peak(arr, i, j):
    # find the midpoint
    mid_point = int((i+j)/2)
    # Edge case - when mid-point is end of array
    if mid_point+1 == len(arr):
        if arr[mid_point] >= arr[mid_point-1]:
          return arr[mid_point]
    # Edge case - when mid-point is start of array
    if mid_point-1 < 0:
        if arr[mid_point] >= arr[mid_point+1]:
            return arr[mid_point]
    # for all other cases
    if arr[mid_point-1] <= arr[mid_point] >= arr[mid_point+1]:
        return arr[mid_point]
    elif arr[mid_point-1] > arr[mid_point]:
        return find_peak(arr,i,mid_point-1)
    elif arr[mid_point+1] > arr[mid_point]:
        return find_peak(arr,mid_point+1,j)


if __name__ == "__main__":
    given_array_1 = [44,18,15,12,1,10,13,88,90,91,0]
    given_array_2 = [6,7,4,3,2,1,4,5]
    print(find_peak(given_array_1,0,len(given_array_1)))
    print(find_peak(given_array_2,0,len(given_array_2)))