'''
Требуется вычислить, сколько раз встречается некоторое 
число X в массиве A[1..N]. Пользователь в первой строке 
вводит натуральное число N – количество 
элементов в массиве. В последующих  строках записаны 
N целых чисел Ai. Последняя строка содержит число X

from random import randint

N = int(input('Input length of array: '))
array = [randint(1, 9) for _ in range(N)]
print(f'Our array is: {array}')
X = randint(1, 9)
print(f'And now my number X is: {X}')
counter = 0
for i in array:
    if i == X:
        counter += 1
    else: 
        i += 1
print(f'Number of coincidence X in our array is: {counter}')
'''

'''
Требуется найти в массиве A[1..N] самый близкий по 
величине элемент к заданному числу X. 
Пользователь в первой строке вводит натуральное число 
N – количество элементов в массиве. 
В последующих  строках записаны N целых чисел Ai. 
Последняя строка содержит число X

from random import randint

N = int(input('Input length of array: '))
array = [randint(1, 9) for _ in range(N)]
print(f'Our array is: {array}')
X = randint(1, 9)
print(f'And now my number X is: {X}')
Num = []
for i in array:
    Num.append(abs(X-i))
Ind = Num.index(min(Num))
print(f'Array number close up to X is: {array[Ind]}')
'''

'''
 В настольной игре Скрабл (Scrabble) каждая буква имеет 
определенную ценность. В случае с английским алфавитом 
очки распределяются так:A, E, I, O, U, L, N, S, T, R 
– 1 очко; D, G – 2 очка; B, C, M, P – 3 очка; 
F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; 
Q, Z – 10 очков. А русские буквы оцениваются так: 
А, В, Е, И, Н, О, Р, С, Т – 1 очко; 
Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка; 
Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; 
Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. 
Напишите программу, которая вычисляет стоимость 
введенного пользователем слова. 
Будем считать, что на вход подается только одно слово, 
которое содержит либо только английские, 
либо только русские буквы.

import re

dict = {
       1: 'AEIOULNSTRАВЕИНОРСТ', 
       2: 'DGДКЛМПУ', 
       3: 'BCMPБГЁЬЯ',
       4: 'FHVWYЙЫ',
       5: 'KЖЗХЦЧ',
       8: 'JXШЭЮ',
       10: 'QZФЩЪ'
        }

Word = input('Input one word on ENG or RUS: ')

result = [key for letter in Word for key, value in dict.items() if letter in value]

print (sum(result))
'''
