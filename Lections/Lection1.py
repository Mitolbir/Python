'''
Форматированный вывод в консоль

print("Input first number: ")
a = int(input())
b = int(input("Input second number: "))

print(a, " + ", b, " = ", a + b)
'''

'''
Округление до 3 знаков после запятой

a = 5.89471
b = 6.8966
print(round(a*b, 3))
'''

'''
Работа буллевой функции

Ложь
a = 1 > 4
print(a)

Правда
a = 1 < 4 and 5 > 2
print(a)

Ложь
a = 1 == 2
print(a)

Правда
a = 1 != 2
print(a)

Правда
a = 'qwe'
b = 'qwe'
print(a == b)

Правда
a = 1 < 3 < 5 < 10
print(a)
'''

'''
Работа else if

if condition1:
    operator
elseif condition2:
    operator
elseif condition3:
    operator
else:
    operator
'''

'''
Работа и/или

if condition1 and condition2:
    operator
if condition3 or condition4:
    operator
'''

'''
Вывод приветствия в зависимости от имени

username = input('Input name: ')
if username == 'Маша':
    print('Ура, это же Маша!')
elif username == 'Марина':
    print('Я так ждала Вас, Марина!')
elif username == 'Ильнар':
    print('Ильнар - топ')
else:
    print('Привет, ', username)
'''

'''
Работа while

Сумма остатков от деления числа на 10

n = 423
summa = 0
while n > 0:
    x = n % 10
    summa = summa + x
    n = n//10
print(summa)
'''

'''
Работа while с else

i = 0
while i < 5:
    #if i == 3:
        #break
    i = i + 1
else:
    print('Пожалуй')
    print('хватит')
print(i)
'''

'''
Метод флажка

n = int(input())
flag = True
i = 2
while flag:
    if n % i == 0: # если остаток при делении числа n на i равен 0
        flag = False
        print(i)
    elif i > n // 2: # делить числа не может превышать введенное число, деленное на 2
        print(n)
        flag = False
    i += 1
'''