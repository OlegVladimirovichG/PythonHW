# 1) Вычислить число c заданной точностью d
# Пример:
# при d = 0.001, π = 3.142 10^(-1) ≤ d ≤10^(-10)

#
# from math import pi
#
# d = int(input('Введите точность округления: '))
# print(round(pi, d))


# 2) Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# num = int(input('Введите число: '))
# lst = []
# simple = 2
# while num > 1:
#     if num % simple == 0:
#         lst.append(simple)
#         num /= simple
#     else:
#         simple += 1
# print(lst)

# 3) Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.

# num_lst = list(map(int, input('Введите последовательность чисел: ').split()))
# uniq_lst = [i for i in num_lst if num_lst.count(i) == 1]
# print(uniq_lst)

# 4) Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2x^2 + 4x + 5 = 0 или x^2 + 5 = 0 или 10x^2 = 0

# from random import randint
# import itertools
#
# k = randint(2, 7)
#
# def get_ratios(k):
#     ratios = [randint(0, 10) for i in range (k + 1)]
#     while ratios[0] == 0:
#         ratios[0] = randint(1, 10)
#     return ratios
#
# def get_polynomial(k, ratios):
#     var = ['*x^']*(k-1) + ['*x']
#     polynomial = [[a, b, c] for a, b, c  in itertools.zip_longest(ratios, var, range(k, 1, -1), fillvalue = '') if a !=0]
#     for x in polynomial:
#         x.append(' + ')
#     polynomial = list(itertools.chain(*polynomial))
#     polynomial[-1] = ' = 0'
#     return "".join(map(str, polynomial)).replace(' 1*x',' x')
#
#
# ratios = get_ratios(k)
# polynom_1 = get_polynomial(k, ratios)
# print(polynom_1)
#
# with open('1st.txt', 'w') as data:
#     data.write(polynom_1)
#
#
# # Второй многочлен для следующей задачи:
#
# k = randint(2, 5)
#
# ratios = get_ratios(k)
# polynom_2 = get_polynomial(k, ratios)
# print(polynom_2)
#
# with open('2nd.txt', 'w') as data:
#     data.write(polynom_2)


# 5) Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

# к этой задаче я вернусь позже. сам решить пока не могу, а списывать - пользы 0