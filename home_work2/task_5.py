# Реализуйте алгоритм перемешивания списка.
 
import random

user_list = list(map(int, input('Введите числовой список: ').split(' ')))
print(user_list)

random.shuffle(user_list)

print(user_list)