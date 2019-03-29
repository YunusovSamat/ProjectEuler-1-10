"""
------------------------------- Задание -------------------------------
Сумма простых чисел меньше 10 равна 2 + 3 + 5 + 7 = 17.
Найдите сумму всех простых чисел меньше двух миллионов.
"""


def eratosthen(n):
    arr = list(range(3, n, 2))
    length = len(arr)
    for i, x in enumerate(arr):
        if x == 0:
            continue
        for j in range(i+x, length, x):
            arr[j] = 0
    arr = list(filter(None, arr))
    return arr


if __name__ == "__main__":
    n = 2000000
    sum_n = sum(eratosthen(n)) + 2
    print(__doc__)
    print("Ответ:", sum_n)
