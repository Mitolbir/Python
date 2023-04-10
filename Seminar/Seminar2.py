'''
Дано натуральное число A > 1. Определите, каким по счету числом 
Фибоначчи оно является, 
то есть выведите такое число n, что φ(n)=A. 
Если А не является числом Фибоначчи, выведите число -1.

Input: 5
Output: 6

Ряд чисел Фибоначчи:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 
1597, 2584, 4181, 6765, 10946, 17711, …

n = int(input('Input natural number: '))
fib1 = 0
fib2 = 1
count = 2
while fib2 < n:
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum
    count += 1

if n == fib2:
    print(count)
else:
    print(-1)
'''

'''
2) Пользователь вводит число N (1 ≤ N ≤ 10). 
Далее построчно N чисел от -50 до 50. 
Нужно вывести наибольшее количество идущих подряд положительных чисел.

Input: 6 -> -20 30 -40 50 10 -10
Output: 2

from random import randint

n = int(input('Input number from 1 to 10: '))
counter1 = 0
counter_max = 0
for _ in range(n):
    number = randint(-50, 50)
    print(number)
    if number > 0:
        counter1 += 1
    elif counter1 > counter_max:
        counter_max = counter1
        counter1 = 0
    else:
        counter1 = 0

if counter1 > counter_max:
    counter_max = counter1

print(f'Neigborhood up to 0 numbers = {counter_max}')
'''

'''
2) Пользователь вводит одно число N. Далее идут N чисел, 
записанных на новой строчке каждое. 
Вывести максимальное и минимальное (циклы)
Input: 5 -> 5 1 6 5 9
Output: 1 9

from random import randint

n = int(input('Input natural number: '))
min_num = 10
max_num = 0
for _ in range(n):
    number = randint(1, 10)
    print(number)
    if number < min_num:
        min_num = number
    if number > max_num:
        max_num = number
print(f'Minimal number = {min_num}, Maximal number = {max_num}')
'''
