import random


def qsort(array):
    if len(array) < 2:
        return array
    else:
        pivot = random.choice(array)
        less = [i for i in array if i < pivot]
        greater = [i for i in array if i > pivot]
        return qsort(less) + [pivot] + qsort(greater)


ls = [5, 8, 3, 9, 4, 1, 7, 2, 6]

print(qsort(ls))

