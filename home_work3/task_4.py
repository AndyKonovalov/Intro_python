# Напишите программу, которая будет преобразовывать десятичное число в двоичное (без встроенных функций).

# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

number = int(input('Введите десятичное число: '))
binary_list = []

while number // 2 >= 1:
    binary_element = number % 2 # остаток
    binary_list.append(binary_element)
    quotient = number // 2 # частное
    if quotient == 1:
        binary_list.append(quotient)
    number = quotient

for i in reversed(binary_list): # разворачиваем список
    print(i, end='')