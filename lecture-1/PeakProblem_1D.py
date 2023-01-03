"""Given an array A with n elements, find any peak element A[i] where A[i] ≥ A[i − 1]
and A[i] ≥ A[i + 1]. For elements on the boundaries of the array, the element only needs to be
greater than or equal to its lone neighbor to be considered a peak."""

"""
1. Find the n/2 element
2. If n/2 element is >= (n/2)-1 and >= (n/2)+1 then return n/2 (It is the peak)
3. if n/2 element is < (n/2) -1 then use logic in steps 1 & 2 on the LHS array i.e Array[0] to Array[(n/2)]  recursively till only 2 elements are left.
4. If step 3 does not give a peak element then use Array[n/2] + 1 to Array[len(Array)] + 1 recursively till only 2 elements are left.
>>
"""
def findPeak(arr,i,j):
    #find the midpoint
    mid_point = int((i+j)/2)
    #Edge case - when mid-point is end of array
    if mid_point+1 == len(arr):
        if arr[mid_point] >= arr[mid_point-1]:
          return arr[mid_point]
    #Edge case - when mid-point is start of array
    if mid_point-1 < 0:
        if arr[mid_point] >= arr[mid_point+1]:
            return arr[mid_point]
    #for all other cases
    if arr[mid_point-1] <= arr[mid_point] >= arr[mid_point+1]:
        return arr[mid_point]
    elif arr[mid_point-1] > arr[mid_point]:
        return findPeak(arr,i,mid_point-1)
    elif arr[mid_point+1] > arr[mid_point]:
        return findPeak(arr,mid_point+1,j)


if __name__ == "__main__":
    given_array_1 = [44,18,15,12,1,10,13,88,90,91,0]
    print(findPeak(given_array_1,0,len(given_array_1)))
    given_array_2 = [6,7,4,3,2,1,4,5]
    print(findPeak(given_array_2,0,len(given_array_2)))