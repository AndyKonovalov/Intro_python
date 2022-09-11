# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 10.01] => 0.19

import random


list_size = int(input('Введите размер списка: '))
my_list = []
res_list =[]

for i in range(list_size):
    my_list.append(round(random.uniform(5, 15), 2))

print(f'Сгенерированный список {my_list}')

for i in my_list:
    res_list.append(i - int(i))
print(f'Разница между максимальным и минимальным значением дробной части элементов списка = {round(max(res_list) - min(res_list), 2)}')