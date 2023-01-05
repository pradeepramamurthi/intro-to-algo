import pprint, random

"""A 2-D peak in a matrix is a location with the property that its four neighbors
(north, south, east, and west) have value less than or equal to the value of the peak 
unless the peak occurs in the 4 edges of the matrix in which case we compare only three neighbours"""

"""
0. Helper Method to create a n X m sized 2-D matrix.
(No need to calculate the Time Complexity of this operation)

Algo Logic:
1. n x m matrix where n is the row and m is the column.
2. First get the mid column of the matrix m/2.  
3. Get the largest value in this column (global max of col.). Time Complexity: O(n)
4. Now check if the globalMax(i,j) of column n >=  (i,j+1) and >= (i,j-1) and >= (i+1,j) and >= (i-1,j). If true return this as Peak element.
5. If step 3 does not give a peak element (evals. False) then if (i,j-1) > (i,j) move to Left of Matrix. Repeat Step 2 to 4. recursively.
6. If step 3 does not give a peak element (evals. False) then if (i,j+1) > (i,j) move to Left of Matrix. Repeat Step 2 to 4. recursively.
5. Edge case: if i = 0 or j = m then check only one neighbour and up and down.
6. The above logic is run in Time Complexity of n O(log n).
   T(n) = O(n) (To Get max of a column with n elements)  + T(n/2) :Running time of half of the input value + O(1) : Constant time to Compare to neighbours
   On every pass: O(n) +(T(n/2) + O(1) + T(n/4) + O(1) + T(n/8) + O(1)....) is repeated till only one Column is left = n O(log n)
"""


def find_2d_peak(gen_array, num_rows, col_start, col_end):

    # Get the Mid-point column of the Matrix
    j = int((col_end-col_start)/2) + col_start
    # max_in_col j
    max_in_col, (i1,j1) = get_max(gen_array, j, num_rows)
    # Set i to 0 ; i represents rows and j represents mid column.
    for i in range(0, num_rows-1):

        # Edge case check when only one col. is left
        if col_start == col_end-1:
            return max_in_col
        # Edge case check when position of global max of a col. occurs in first row
        if i1 == 0:
            if gen_array[i1][j1+1] <= max_in_col >= gen_array[i1][j1-1] and gen_array[i1+1][j1] <= max_in_col:
                return max_in_col
        # Edge case check when position of global max of a col. occurs in first row
        if i1 == num_rows-1:
            if gen_array[i1][j1+1] <= max_in_col >= gen_array[i1][j1-1] and max_in_col >= gen_array[i1-1][j1]:
                return max_in_col
        # check all 4 neighbours
        if gen_array[i1][j1+1] <= max_in_col >= gen_array[i1][j1-1] and gen_array[i1+1][j1] <= max_in_col >= gen_array[i1-1][j1]:
            return max_in_col
        # when LHS element is greater than mid-element - then select left set of matrix
        if max_in_col < gen_array[i1][j1-1]:
            return find_2d_peak(gen_array, num_rows, 0, j1)
        # when RHS element is greater than mid-element - then select right set of matrix
        elif max_in_col < gen_array[i1][j1+1]:
            return find_2d_peak(gen_array, num_rows, j1+1, col_end)


# function to return global max and its position in a column j of the array
def get_max(gen_array, j, num_rows):
    loc = ()
    max_in_col = gen_array[0][j]
    loc = (0,j)
    for i in range(0, num_rows-1):
        if gen_array[i+1][j] > max_in_col:
            max_in_col = gen_array[i+1][j]
            loc = (i+1, j)
    return max_in_col, loc


def generate_2d_matrx(rows, cols, max_number):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(random.randrange(max_number))
        matrix.append(row)
    return matrix


if __name__ == "__main__":
    generated = [[628, 430, 1001], [100, 649, 915], [800, 504, 12]]
    generated2 = [[20, 505, 505, 606], [71, 500, 500, 62], [28, 1001, 300, 81], [29, 90, 100, 21]]
    generated3 = [[20, 506, 505, 505], [71, 500, 505, 62], [28, 1001, 300, 81], [29, 1002, 100, 21]]
    generated4 = [[507, 506, 505, 505], [1071, 500, 505, 62], [28, 101, 300, 81], [29, 100, 100, 21]]
    print(find_2d_peak(generated, 3, 0, 3))
    print(find_2d_peak(generated2, 4, 0, 4))
    print(find_2d_peak(generated3, 4, 0, 4))
    print(find_2d_peak(generated4, 4, 0, 4))

