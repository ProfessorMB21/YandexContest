
# we need an array of n elements
# calculate the number pairs of inversions in the array
# output result of calculation

print("py")


n = int(input())
vals = list(map(int, input().split()))

arr = [x for x in vals]


def counting_sort(lst: list):
    max_val = max(lst)
    count = [0] * (max_val + 1)

    while len(lst) > 0:
        num = arr.pop(0)
        count[num] += 1

    for i in range(len(count)):
        while count[i] > 0:
            lst.append(i)
            count[i] -= 1

    return lst


counting_sort(arr)

for x in arr:
    print(x, end=" ")

