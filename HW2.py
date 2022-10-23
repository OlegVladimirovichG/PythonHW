# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

num, summ = input('Введите число: '), 0
num = num.replace('-', '')
num = num.replace(',', '')
num = num.replace('.', '')
for i in range(len(num)):
    summ += int(num[i])
print(summ)

for i in range(len(num)):
    summ += int(num[i])
print(summ)



#
# 2 –Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
#
# n = int(input('Введите число: '))
# count = 1
# f = []
# for i in range(1, n + 1):
#     count *= i
#     f.append(count)
# print(f'Набор произведений чисел от 1 до {n}: {f}')
#
# 3 – Задайте список из n чисел последовательности (1 + 1 / n) ** n и выведите на экран их сумму.
#
# Пример:
# 1 -> 2.0
# 2 -> 4.25
# 3 -> 6.62037037037037
#
# n = int(input('Введите число: '))
# summ = 0
# for i in range(1, n+1):
#     summ += (1+1 / i) ** i
# print(summ)
#
# 4 – Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

# from random import randint
#
# num = []
# n = int(input('Введите число: '))
# for i in range(n):
#     num.append(randint(-n, n))
# print(f'Рэндомный список: {num}')
#
# mult = 1
# index = []
# lst = []
# with open('file.txt', 'r') as file:
#     for i in file:
#         if int(i) < len(num):
#             index.append(int(i))
#             mult *= num[int(i)]
#             lst.append(num[int(i)])
#
# print(f'Индекс из файла: {index}')
# print(f'Выборка, согласно индексу: {lst}')
# print(f'Результат умножения: {mult}')

# 5 – Реализуйте алгоритм перемешивания списк
#
# import random
# l = [1, 2, 3, 4, 5]
# random.shuffle(l)
# print(l)