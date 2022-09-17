# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# "20" -> [2, 2, 5]


num = int(input("Введите число: "))
i = 2 # первое простое число
res_list = []
user_data = num
while i <= num:
    if num % i == 0:
        res_list.append(i)
        num //= i
    else:
        i += 1
print(f'Простые множители числа {user_data} следующие: {res_list}')
