# Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.
# [1, 1, 2, 3, 4, 5, 5] -> [2, 3, 4]

user_input = input('Задайте последовательность чисел через пробел: ').split(' ')
numbers = []
found = set() # создаем пустые множества
found_again = set()

for i in user_input:
    numbers.append(int(i))
print(f'Введенный список: {numbers}')

for number in numbers:
    if number in found_again: # если элемент списка есть в множетсве found_again, то проверяем следующий элемент списка
        continue
    if number in found:
        found.remove(number)
        found_again.add(number) # собирает повторяющиеся элементы
    else:
        found.add(number)

print(f'Список из неповторяющихся элементов: {list(found)}') 