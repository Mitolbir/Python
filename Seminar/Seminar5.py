'''
Последовательностью Фибоначчи называется последовательность чисел 
a0, a1, ..., an, ..., где
a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
Требуется найти N-е число Фибоначчи
Input: 7
Output: 13
Задание необходимо решать через рекурсию

def fib(n):
        if n < 2:
              return n
        else:
            return fib(n-1) + fib(n-2)
print(fib(7))
'''

'''
Хакер Василий получил доступ к классному журналу и хочет заменить все свои 
минимальные оценки на максимальные. Напишите программу, которая заменяет 
оценки Василия, но наоборот: все максимальные – на минимальные.
Input: 5 -> 1 3 3 3 4
Output: 1 3 3 3 1

import random
def grade(n):
    list_1 = []
    for i in range(n):
        list_1.append(random.randint(1,5))
    print(list_1)
    minimum = min(list_1)
    maximum = max(list_1)
    for i in range(n):
        if list_1[i] == maximum:
            list_1[i] = minimum
    return list_1

print(grade(10))
'''

'''
Напишите функцию, которая принимает одно число и
проверяет, является ли оно простым
Напоминание: Простое число - это число, которое
имеет 2 делителя: 1 и n(само число)
Input: 5
Output: yes

def prime(n):
    for i in range(2, n):
        if n % i == 0:
            return "no"
        return "yes"

print(prime(13))
'''

'''
Дано натуральное число N и последовательность из N элементов. 
Требуется вывести эту последовательность в обратном порядке.
Примечание. В программе запрещается объявлять массивы и использовать циклы 
(даже для ввода и вывода).
Input: 2 -> 3 4
Output: 4 3

def reverse(num):
    if num <= 0:
        return
    user = int(input("Input number: "))
    reverse(num - 1)
    print(user, end = " ")

number = int(input("Input number: "))
reverse(number)
'''