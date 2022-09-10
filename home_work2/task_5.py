# Реализуйте алгоритм перемешивания списка.
 
user_list = list(map(int, input('Введите числовой список: ').split(' ')))
print(user_list)
 
user_list[::2], user_list[1::2] = user_list[1::2], user_list[::2] # меняем четные индексы на нечетные

print(user_list)