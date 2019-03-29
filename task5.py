"""
------------------------------- Задание -------------------------------
2520 - самое маленькое число, которое делится без остатка на все числа
от 1 до 10.
Какое самое маленькое число делится нацело на все числа от 1 до 20?
"""


def split_num(a, arr):
    if a == 1:
        return
    else:
        for p in range(2, a + 1):
            if a % p == 0:
                arr.append(p)
                split_num(a // p, arr)
                return


if __name__ == '__main__':
    arr_n = []
    arr_split = []
    for x in range(2, 21):
        split_num(x, arr_split)
        arr_n.append(arr_split)
        arr_split = []

    min_n = 1
    for x in arr_n:
        t = min_n
        for y in x:
            if t % y == 0:
                t = t // y
            else:
                min_n *= y
    print(__doc__)
    print("Ответ:", min_n)
