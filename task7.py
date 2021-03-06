"""
------------------------------- Задание -------------------------------
Выписав первые шесть простых чисел, получим 2, 3, 5, 7, 11 и 13.
Очевидно, что 6-ое простое число - 13.
Какое число является 10001-ым простым числом?
"""

import math

arr = [3, 5]
count_n = 3
i = 7
while count_n != 10001:
    for x in arr:
        if math.ceil(math.sqrt(i)) < x:
            arr.append(i)
            count_n += 1
            break
        if i % x == 0:
            break
    i += 2

print(__doc__)
print("Ответ:", arr[-1])
