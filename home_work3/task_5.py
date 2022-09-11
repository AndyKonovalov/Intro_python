# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

number = int(input('Введите число k: '))
first_element = 0
second_element = 1
positive_list = [0, 1]
negative_list = [1]

def fibonacci_list(list, element_1, element_2, size):
    for i in range(size - 1):
        next_element = element_1 + element_2
        list.append(next_element)
        element_1 = element_2
        element_2 = next_element
    return list

def n_fibonacci_list(lst, elemnt_1, elemnt_2, length):
    for i in range(length - 1):
        next_element = elemnt_1 - elemnt_2
        lst.append(next_element)
        elemnt_1 = elemnt_2
        elemnt_2 = next_element
    return list(reversed(lst))

print(n_fibonacci_list(negative_list, first_element, second_element, number) + fibonacci_list(positive_list, first_element, second_element, number))