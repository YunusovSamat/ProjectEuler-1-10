"""
------------------------------- Задание -------------------------------
Простые делители числа 13195 - это 5, 7, 13 и 29.
Каков самый большой делитель числа 600851475143,
являющийся простым числом?
"""

import math

n = 600851475143
arr = []
for i in range(3, int(math.sqrt(n)) + 1, 2):
    if n % i == 0:
        arr.insert(len(arr)//2, i)
        arr.insert(len(arr)//2 + 1, n//i)
print(arr)

for i in range(1, len(arr)):
    for j in arr[:i]:
        if arr[i] % j == 0:
            break
    else:
        n = arr[i]
print(__doc__)
print("Ответ:", n)
