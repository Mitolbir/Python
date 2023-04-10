'''
Напишите программу, которая на вход принимает два числа А и В, и возводит
число А в целую степень В с помощью рекурсии

def pow(numA, numB):
    if numB == 0:
        return 1
    elif numB % 2 == 1:
        return pow(numA, numB - 1) * numA
    else:
        return pow(numA, numB // 2) ** 2

A = int(input("Input number A: "))
B = int(input("Input number B: "))
pow(A, B)
print(pow(A, B))
'''

'''
Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых 
неотрицательных чисел. Из всех арифметических операций допускаются 
только +1 и -1. Также нельзя использовать циклы.

def sum(numA, numB):
    numA += 1
    numB -= 1
    if numB > 0:
        return sum(numA, numB)
    else:
        return numA

A = int(input("Input number A: "))
B = int(input("Input number B: "))
sum(A, B)
print(sum(A, B))
'''