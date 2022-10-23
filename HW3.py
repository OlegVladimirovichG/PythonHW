# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#
# Пример:
#
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random
rnd_lst = [random.randint(0, 10) for _ in range(6)]
new_lst = []
mult = 1
for i in range((len(rnd_lst) + 1) // 2):
    mult = rnd_lst[i] * rnd_lst[-i-1]
    new_lst.append(mult)
print(rnd_lst)
print(new_lst)




# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#
# Пример:
#
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.2

from decimal import *

lst = [1.1, 1.2, 3.1, 5.0001, 10.01]
min, max = 1, 0
for element in lst:
    element = str(element)
    element = element.split('.') if '.' in element else ['0', '0']
    fract_part = int(element[1]) / 10 ** len(element[1])
    if fract_part > max:
        max = fract_part
    if fract_part < min:
        min = fract_part
print(f'\nMin = {min}, Max = {max}:')
print(f'Разница = {Decimal(str(max)) - Decimal(str(min))}')



# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#
# Пример:
#
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

num = int(input('Введите число для приобразоания: '))
lst = []
rest = 0
while num > 0:
    rest = num // 2 + num % 2
    if num % 2 == 0:
        lst.append(0)
    else:
        lst.append(1)
    num -= rest
lst.reverse()
print(*lst, sep = '')



# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#
# Пример:
#
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

n = int(input('Введите число: '))
fib = []
nega = []
for i in range(n + 1):
    if i == 0:
        fib.append(0)
    elif i == 1:
        fib.append(1)
    else:
        fib.append(fib[i - 1] + fib[1 - 2])
for i in range(n, 0, -1):
    nega.append(((-1) ** (i + 1)) * fib[i])
print('Для k = ', n, end = '--> ')
print(nega + fib)