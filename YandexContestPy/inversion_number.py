# count the number of index pairs for which the array A[i] > A[j]
# the first line contains an integer n
# the second line contains an array of n natural numbers

n = int(input())

arr = list(map(int, input().split()))

lst = [arr[i] for i in range(n)]

def calculateInversionNumber(lst: list):
    count = 0
    j = 0
    mid = len(lst) // 2

    for i in range(mid):
        mid = len(lst) // 2
        for j in range(mid+1, n):
            if lst[i] > lst[j]:
                count += 1


    return count

print(calculateInversionNumber(lst))
