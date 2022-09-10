# Задайте список из k чисел последовательности (1 + 1\k)^k и выведите на экран их сумму.

number_k = float(input('Введите число k: '))
list = []
i = 1 # левая граница значений 1 до k
x = 1 # элементы последовательности (1 + 1\k)^k
summ_list = 0

while i <= number_k:
    x = round((1 + 1/i)**i, 2)
    list.append(x)
    summ_list += x
    i += 1
print(f'Сумма элементов списка {list} из k чисел = {summ_list}')