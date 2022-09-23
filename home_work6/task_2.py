# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:
# - 0,56 -> 11

# старый код

# from curses.ascii import isdigit

# number = input('Введите десятичную дробь: ')
# summ_digit = 0

# for i in number:
#     if i.isdigit():
#         summ_digit += int(i)
# print(f'Сумма цифр десятичной дроби = {summ_digit}')

# новый код

number = input('Введите десятичную дробь: ')

new_sum = sum(map(int, str(number).replace('.', ''))) # использовал метод map для перевода элементов строки в числа
print(f"Сумма цифр вещественного числа равна = {new_sum}")

