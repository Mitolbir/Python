'''
Напишите программу, которая принимает на вход строку, и отслеживает, 
сколько раз каждый символ уже встречался. Количество повторов добавляется к 
символам с помощью постфикса формата _n.
Input: a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
Для решения данной задачи используйте функцию .split()

word = input("Input word: ").split()
dict = dict()

for letter in word:
    print(letter, end = "")
    if letter not in dict:
        dict[letter] = 0
    else:
        dict[letter] += 1
        print("_", dict[letter], sep = "", end = "")
    print(end = " ")
'''

'''
Пользователь вводит текст(строка). Словом считается последовательность 
непробельных символов идущих подряд, слова разделены одним или большим числом 
пробелов. Определите, сколько различных слов содержится в этом тексте.
Input: She sells sea shells on the sea shore The shells that she sells are 
sea shells I'm sure So if she sells sea shells on the sea shore I'm sure 
that the shells are sea shore shells
Output: 13

text = """She sells sea shells on the sea shore The shells that she sells are 
sea shells I'm sure So if she sells sea shells on the sea shore I'm sure 
that the shells are sea shore shells""".lower().split()

print(text)

uniq = set(text)
print(len(uniq))
'''

'''
1) Ваня и Петя поспорили, кто быстрее решит следующую задачу: 
“Задана последовательность неотрицательных целых чисел. 
Требуется определить значение наибольшего элемента последовательности, 
которая завершается первым встретившимся нулем (число 0 не входит в 
последовательность)”. Однако 2 друга оказались не такими смышлеными. 
Никто из ребят не смог до конца сделать это задание. 
Они решили так: у кого будет меньше ошибок в коде, тот и выиграл спор. 
За помощью товарищи обратились к Вам, студентам

n = int(input())
max_number = n
while n != 0:
    n = int(input())
    if max_number < n:
        max_number = n
print(max_number)
'''
