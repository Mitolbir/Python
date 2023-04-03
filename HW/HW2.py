'''
Пользователь вводит число n. На следующих строках нужно вводить 1 или 0, 
в ответе вывести количество наименее встречающихся из них 
(т.е либо количество 0 либо 1, в зависимости от того, кого меньше)

from random import randint

n = int(input('Input number: '))
counter0 = 0
counter1 = 0
for _ in range(n):
    number = randint(0, 1)
    print(number)
    if number == 0:
        counter0 += 1
    else:
        counter1 += 1

if counter0 < counter1:
    print(f'0 numbers lesser = {counter0} vs {counter1}')
elif counter0 > counter1:
    print(f'1 numbers lesser = {counter1} vs {counter0}')
else:
    print(f'0 and 1 have equal count of numbers')
'''

'''
Пользователь вводит два числа построчно, первое – сумма двух чисел, 
второе – произведение этих чисел. Нужно вывести исходные числа.

sum = 5
prod = 6
first = 0
second = 0

while first < 100 and second < 100:
    first+=1
    if first + second == sum and first * second == prod:
        print(sum, prod, first, second)
        break
    else:
        second+=1
        if first + second == sum and first * second == prod:
            print(sum, prod, first, second)
            break
'''

'''
Требуется вывести все целые степени двойки (т.е. числа вида 2k), 
не превосходящие числа N.

from random import randint

number = randint(2, 99)
print(number)
step = 1

while step <= number:
    if(step <= number):
        if(step * 2 > number):
            break
        else:
            step = step * 2
            print(step)
'''