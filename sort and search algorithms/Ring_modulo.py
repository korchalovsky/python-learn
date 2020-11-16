# Нахождение обратного элемента в кольце по модулю
n = int(input('Введите величину модуля: '))
a = int(input('Введите число, для которого требуется найти обратный элемент: '))


def func(n, a):
    x1, x2, x3 = 1, 0, n
    y1, y2, y3 = 0, 1, a

    while y3 != 1 and y3 != 0:
        q = x3 // y3
        t1 = x1 - q * y1
        t2 = x2 - q * y2
        t3 = x3 - q * y3
        x1, x2, x3 = y1, y2, y3
        y1, y2, y3 = t1, t2, t3
    if y3 == 0:
        print('Обратного элемента не существует')
    if y3 == 1:
        res = y2
        if res < 0:
            res = res + n
        print('Обратный элемент - ', res)


func(n, a)