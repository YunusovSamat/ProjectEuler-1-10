"""
------------------------------- Задание -------------------------------
Число-палиндром с обеих сторон (справа налево и слева направо) читается
одинаково. Самое большое число-палиндром, полученное умножением двух
двузначных чисел – 9009 = 91 × 99.
Найдите самый большой палиндром, полученный умножением двух
трехзначных чисел.
"""

flag_brk = False

for i in range(997, 99, -1):
    n = int(str(i) + str(i)[::-1])
    for x in range(999, 99, -1):
        if n % x == 0:
            y = n // x
            if (y >= 100) and (y < 1000):
                # print(x, "*", y, "=", n)
                flag_brk = True
                break
    if flag_brk:
        break
print(__doc__)
print("Ответ:", x, y)
