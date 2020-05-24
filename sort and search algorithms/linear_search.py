def linear_search(list_, value):
    for i in range(len(list_)):
        if list_[i] == value:
            return print(i)
    return print('Такого значения нет')


ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
linear_search(ls, 10)
