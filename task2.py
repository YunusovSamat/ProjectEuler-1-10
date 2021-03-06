"""
------------------------------- Задание -------------------------------
Каждый следующий элемент ряда Фибоначчи получается при сложении двух
предыдущих. Начиная с 1 и 2, первые 10 элементов будут:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
Найдите сумму всех четных элементов ряда Фибоначчи, которые не
превышают четыре миллиона.
"""
bgn = 1
end = 2
sum_f = end

while sum_f < 4000000:
    bgn, end = end, bgn + end
    if end % 2 == 0:
        sum_f += end
print(__doc__)
print("Ответ:", sum_f)
