"""
Let R denote the reserved landing times: R = (41, 46, 49, 56) and k = 3
Add t to the set if no other landings are scheduled within k minutes either way. Assume k can vary (i.e. user's input)
When plane lands it is removed from R.

This example implements in O(nlog n) - non-binary tree version
"""

def runway_reserve(k, t):
    R = [39, 40, 45, 51]
    now = 39

    for i in range(0, len(R)):
        if t < now:
            return "t in past - cannot insert"
        if abs(t-R[i]) < k:
            return "error: no place to insert within R"
    R.append(t)

    return merge_sort(R)


"""Note: for merge Sort Time Complexity O(n logn)"""

def merge_sort(R):
    mid = len(R)//2
    """base case where if length of input is 1 element , means it is already sorted"""
    if len(R) == 1:
        return R
    LHS = merge_sort(R[:mid])
    RHS = merge_sort(R[mid:])

    return merge(LHS, RHS)

def merge(LHS, RHS):
    result = []
    l_pointer = 0
    r_pointer = 0
    while l_pointer < len(LHS) and r_pointer < len(RHS):
        if LHS[l_pointer] < RHS[r_pointer]:
            result.append(LHS[l_pointer])
            l_pointer += 1
        else:
            result.append(RHS[r_pointer])
            r_pointer += 1
    if l_pointer < len(LHS):
        result.extend(LHS[l_pointer:])
    if r_pointer < len(RHS):
        result.extend(RHS[r_pointer:])

    return result



if __name__ == "__main__":

    k = 3
    t = 48
    print(runway_reserve(k, t))