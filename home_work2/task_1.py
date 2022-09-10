# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:
# - 0,56 -> 11

from curses.ascii import isdigit


number = input('Введите десятичную дробь: ')
summ_digit = 0

for i in number:
    if i.isdigit():
        summ_digit += int(i)
print(summ_digit)
