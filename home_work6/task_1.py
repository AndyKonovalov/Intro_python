# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных индексы элементы 3 и 9, ответ: 12

# Старый код

# list_size = int(input('Введите размер списка: '))
# list = []
# summ = 0

# def list_generator(my_list, size):
#     for i in range(size):
#         my_list.append(randint(-5, 5))
#     return my_list

# def summ_odd_indexes(some_list, some_summ):
#     for i in some_list[1::2]:
#         some_summ += i
#     return some_summ

# print(f'Сгенерированный список {list_generator(list, list_size)}')
# print(f'Сумма элементов на нечетных позициях списка = {summ_odd_indexes(list, summ)}')

# Слегка обновленный код

from random import randint

list_size = int(input('Введите размер списка: '))
summ = 0

my_list = [randint(-5, 5) for item in range(list_size)] # сократил код через list comprehension

def summ_odd_indexes(some_list, some_summ):
    for i in some_list[1::2]:
        some_summ += i
    return some_summ

print(f'Сгенерированный список {my_list}')
print(f'Сумма элементов на нечетных позициях списка = {summ_odd_indexes(my_list, summ)}')