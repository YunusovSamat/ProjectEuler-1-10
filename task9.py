"""
------------------------------- Задание -------------------------------
Тройка Пифагора - три натуральных числа a < b < c, для которых
выполняется равенство a^2 + b^2 = c^2
Например, 32 + 42 = 9 + 16 = 25 = 52.
Существует только одна тройка Пифагора, для которой a + b + c = 1000.
Найдите произведение abc.
"""

import math

flag = False
for a in range(1, 332):
    for b in range(a+1, 500):
        c = math.sqrt(a**2 + b**2)
        if c.is_integer():
            c = int(c)
            if a + b + c == 1000:
                flag = True
                break
    if flag:
        break

print(__doc__)
print("Ответ:", a * b * c)
