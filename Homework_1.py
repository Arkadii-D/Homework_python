"""
Задача 1
Найдите сумму цифр трехзначного числа
"""
number = int(input('Введите трехзначное число: '))
while number // 1000 > 0 :
    if number//1000 > 0:
        print('Число не трехзначное')
        number = int(input('Введите трехзначное число: '))

sum = 0
while number / 10 > 0:
    sum = sum + number % 10
    number //= 10

print(f'Сумма цифр трехзначного числа равна: {sum}')

"""
Задача 4
Петя, Катя и Сережа делают из бумаги журавликов.
Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, 
если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
Пример:
6 -> 1 4 1
24 -> 4 16 4
60 -> 10 40 10
"""

S = int(input("Введите общее количество журавликов: "))
if not S % 6:
     x = S // 6
     print(f'Катя {x * 4} ')
     print(f'Сережа {x} ')
     print(f'Петя {x}')

"""
Задача 6
Вы пользуетесь общественным транспортом? 
Вероятно, вы расплачивались за проезд и получали билет с номером. 
Счастливым билетом называют такой билет с шестизначным номером, 
где сумма первых трех цифр равна сумме последних трех. 
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
Вам требуется написать программу, которая проверяет счастливость билета.
Пример:
385916 -> yes
123456 -> nо
"""

while True:
    number = input('Введите шестизначный номер Вашего билета: ')
    if number.isdigit() and len(number) == 6:
        if sum(map(int, number[:3])) == sum(map(int, number[3:])):
            print('Ура, Ваш билет счастливый!')
        else:
            print('Увы, Ваш билет не счастливый(')
        break
    else:
        print('Введен некорректный номер билета, попробуйте еще раз)')