# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных пользователем через пробел позициях.

from random import randint


list_size = int(input('Введите размер списка: '))
positions_list = list(map(int, input('Введите позиции элементов через пробел: ').split(' ')))
# positions_list = list(map(int, positions))
start_list = []
multiply_res = 1
for i in range(list_size):
    start_list.append(randint(-list_size, list_size))
print(f'Сгенерированный список {start_list}')
print(f'Список введенных позиций: {positions_list}')

for i in positions_list:
    if i < list_size:
        multiply_res *= start_list[i]

print(f'Произведение элементов на указанных позициях = {multiply_res}')