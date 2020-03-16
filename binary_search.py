def binary_search(list, value):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == value:
            return mid
        elif guess >= value:
            high = mid - 1
        else:
            low = mid + 1
    return None


array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(binary_search(array, 5))
