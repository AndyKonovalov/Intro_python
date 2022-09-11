# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from random import randint

list_size = int(input('Введите размер списка: '))
user_list = []
product_list =[]
even_check = 1
if list_size % 2 == 0: # проверка четности, нечетности размера списка
    even_check = 0

for i in range(list_size):
    user_list.append(randint(0, 10))

print(f'Сгенерированный список {user_list}') 

for i in range(list_size // 2 + even_check): # длина нового списка 
    product_list.append(user_list[i] * user_list[list_size - i - 1])
    if i == list_size - i - 1:
        product_list[i] = user_list[i] * user_list[i] # следуя логике примера к дз, элемент, у которого нет пары умножается сам на себя
print(f'Произведения пар чисел из данного списка следующие: {product_list}')