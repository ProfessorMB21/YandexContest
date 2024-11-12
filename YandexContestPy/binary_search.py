
# Binary search
# In the first line, input an integer n and enter an array A of n different natural numbers, in ascending order,
# In the second line, input an integer k and enter an array of k natural numbers.
# For each integer from 1 to k, output the index 1 <= j <= n, for which A[j] is equal to the integer,
# otherwise, output -1 if no such number exists.

n = list(map(int, input().split()))
lst = [n[i] for i in range(len(n)) if i > 0]

k = list(map(int, input().split()))
lst2 = [k[i] for i in range(1, len(k))]


def binary_search(val: int, arr1: list):
    left = 0
    right = arr1.__len__() - 1

    while left <= right:
        mid_index = (left + right) // 2
        if arr1[mid_index] == val:
            return mid_index + 1
    
        if arr1[mid_index] < val:
            left = mid_index + 1
        elif arr1[mid_index] > val:
            right = mid_index - 1
    
    return -1       # not found


for x in lst2:
    print(binary_search(x, lst), end=" ")
print()