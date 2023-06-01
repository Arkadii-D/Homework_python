"""
Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь
в первой строке вводит натуральное число N – количество элементов в массиве. В последующих строках
записаны N целых чисел Ai. Последняя строка содержит число X
n = 5
1 2 3 4 5
x = 3

 -> 1
"""

N = abs(int(input('Введите количество элементов списка А: ')))
A_entered = input("Введите через пробел элементы списка: ").split()
A_num = list(map(int, A_entered))
if len(A_num) != N:
    print('Введенные элементы не соответствуют заявленному количеству!')
else:
    X = int(input('Введите число X, которое необходимо найти в списке: '))
    count = 0
    for i in range(N):
        if A_num[i] == X:
            count += 1
    print(f'Число {X} встречается в списке A {count} раз')

"""
Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент
к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество
элементов в массиве. В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

n = 5
1 2 3 4 5
x = 6
-> 5
"""

N = abs(int(input('Введите количество элементов списка А: ')))
A_entered = input("Введите через пробел элементы списка: ").split()
A_num = list(map(int, A_entered))
if len(A_num) != N or N == 0:
    print('Введенные элементы не соответствуют заявленному количеству!')
else:
    X = int(input('Введите число X, с которым необходимо сравнивать элементы списка: '))
    min = abs(X - A_num[0])
    index = 0
    for i in range(1, N):
        count = abs(X - A_num[i])
        if count < min:
            min = count
            index = i
    print(f'Число {A_num[index]} в списке A наиболее близко по величине к числу {X}, их разница составляет {abs(X - A_num[index])}')

    """
    Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет
    определенную ценность. В случае с английским алфавитом очки распределяются так:
    A, E, I, O, U, L, N, S, T, R – 1 очко;
    D, G – 2 очка;
    B, C, M, P – 3 очка;
    F, H, V, W, Y – 4 очка;
    K – 5 очков;
    J, X – 8 очков;
    Q, Z – 10 очков.
    А русские буквы оцениваются так:
    А, В, Е, И, Н, О, Р, С, Т – 1 очко;
    Д, К, Л, М, П, У – 2 очка;
    Б, Г, Ё, Ь, Я – 3 очка;
    Й, Ы – 4 очка;
    Ж, З, Х, Ц, Ч – 5 очков;
    Ш, Э, Ю – 8 очков;
    Ф, Щ, Ъ – 10 очков.
    Напишите программу, которая вычисляет стоимость введенного пользователем слова.
    Будем считать, что на вход подается только одно слово, которое содержит либо
    только английские, либо только русские буквы.

    Ввод:
    ноутбук
    Вывод:
    12
    """
    eng = {1: 'AEIOULNSTR',
           2: 'DG',
           3: 'BCMP',
           4: 'FHVWY',
           5: 'K',
           8: 'JZ',
           10: 'QZ'}
    rus = {1: 'АВЕИНОРСТ',
           2: 'ДКЛМПУ',
           3: 'БГЁЬЯ',
           4: 'ЙЫ',
           5: 'ЖЗХЦЧ',
           8: 'ШЭЮ',
           10: 'ФЩЪ'}
    N = abs(int(input('Введите 1, если играем в английской раскладке, либо 0, если в русской: ')))
    word = input('Введите слово: ').upper()
    if N == 1:
        print('За это слово вы получаете', sum([k for i in word for k, v in eng.items() if i in v]), 'очков')
    elif N == 0:
        print('За это слово вы получаете', sum([k for i in word for k, v in rus.items() if i in v]), 'очков')
    else:
        print('Вы мухлюете и играете не по правилам!')