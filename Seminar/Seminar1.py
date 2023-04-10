'''
За день машина проезжает n километров. Сколько дней нужно, чтобы проехать
маршрут длиной s километров? При решении этой задачи нельзя пользоваться
условной конструкцией if и циклами.

import math
n = int(input('Input number of km per day = '))
s = int(input('Input number of km = '))
print(math.ceil(s/n))

# day = s + (n - 1)//n - альтернативный вариант
# print(f"{day} - number of days)
'''

'''
В некоторой школе решили набрать три новых математических класса и
оборудовать кабинеты для них новыми партами. За каждой партой может
сидеть два учащихся. Известно количество учащихся в каждом из трех классов.
Выведете наименьшее число парт, которое нужно приобрести для них.

import math
print('Input number of students in first class = ')
a = int(input())
print('Input number of students in second class = ')
b = int(input())
print('Input number of students in third class = ')
c = int(input())

q = math.ceil(a/2)
w = math.ceil(b/2)
e = math.ceil(c/2)
print(f'Number of tables in first class = {q}')
print(f'Number of tables in second class = {w}')
print(f'Number of tables in third class = {e}')
print('Number of all tables = ', q + w + e)
'''

'''
Вагоны в электричке пронумерованы натуральными числами, начиная с 1.
В каждом вагоне написан его номер. Витя сел в i-й вагон от головы поезда
и обнаружил, что его вагон имеет номер j. Он хочет определить, сколько всего
вагонов в электричке. Напишите программу, которая будет это делать или
сообщать, что без дополнительной информации это сделать невозможно.

number = int(input('Wagon number i: '))
reverse = int(input('Wagon number j: '))
if number == reverse:
    print('We need more information')
else:
    print('Wagons in train ', number + reverse - 1)
'''

'''
Дано натуральное число - год. Требуется определить, является ли год с 
данным номером високосным. Если год является високосным, то выведите YES, 
иначе выведите NO. Напомним, что в соответствии с григорианским календарем, 
год является високосным, (если его номер кратен 4, но не кратен 100), 
а также если он кратен 400.

year = int(input('Input year: '))
if year % 4 == 0 and year % 100 != 0:
    print('Yes')
elif year % 400 == 0:
    print('Yes')
else:
    print('No')
'''
