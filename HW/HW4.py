'''
Пользователь вводит 2 числа. n - кол-во элементов первого множества. 
m - кол-во элементов второго множества. Затем пользователь вводит сами 
элементы множеств (может быть с повторениями).
Выдать без повторений в порядке возрастания все те числа, которые встречаются 
в обоих наборах.

from random import randint

n = randint(5, 15)
print(f'Number of first set: {n}')
m = randint(5, 15)
print(f'Number of second set: {m}')

array1 = [randint(1, 20) for _ in range(n)]
print(f'First set: {array1}')
array2 = [randint(1, 20) for _ in range(m)]
print(f'Second set: {array2}')

uniq1 = set(array1)
print(f'First uniq set: {uniq1}')
uniq2 = set(array2)
print(f'Second uniq set: {uniq2}')

final = []
for i in uniq1:
    for j in uniq2:
        if i == j:
            final.append(i)
print(f'Set with both sorted numbers: {final}')
'''

'''
В фермерском хозяйстве в Карелии выращивают чернику. 
Она растет на круглой грядке, причем кусты высажены только по окружности. 
Таким образом, у каждого куста есть ровно два соседних. 
Всего на грядке растет N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них 
выросло различное число ягод – на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
Собирающий модуль за один заход, находясь непосредственно перед некоторым 
кустом, собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, 
которое может собрать за один заход собирающий модуль, 
находясь перед некоторым кустом заданной во входном файле грядки.

from random import randint

N = randint(3, 9)
print(f'Number of strawberry bushes: {N}')

bushes = [randint(1, 20) for _ in range(N)]
print(f'Number of berries on every bush: {bushes}')

maximal = 0
for bush in range(len(bushes)-1):
    maximal = max(maximal, bushes[bush-1] + bushes[bush] + bushes[bush+1])
print(f'Max number of berries at 3 bushes is: {maximal}')
'''