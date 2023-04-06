'''
Задача 1.1 Создать рандомный список и показать кол-во
уникальных элментов во множестве

from random import randint

list_1 = []

for _ in range(randint(3, 10)):
    number = randint(-10, 10)
    print(number, end = ' ')
    list_1.append(number)

set_1 = set(list_1)
print()
print(len(set_1))
'''

'''
Задача 1.2 Создать рандомный список и показать кол-во
уникальных элментов во множестве генератором списков

from random import randint

list_1 = [randint(-10, 10) for _ in range(randint(5, 15))]
print(list_1)

set_1 = set(list_1)
print(len(set_1))
'''

'''
Дана последовательность из N чисел и число K. Необходимо
сдинуть всю последовательность на K элементов вправо,
K - положительное число.

list_1 = []
for i in range(1, 6):
    list_1.append(i)
print(list_1)

k = int(input('Input switch number: '))
for i in range(k):
    list_1.append(list_1.pop(0))

print(list_1)
'''

'''
Напишите программу для печати всех уникальных значений
в словаре

dict = [{'V': 'S001'}, {'V':'S002'}, {'VI': 'S001'}]
print(dict)
my_set = set()
for dict_i in dict:
    for key in dict_i:
        my_set.add(dict_i[key].strip())
print(my_set)
'''