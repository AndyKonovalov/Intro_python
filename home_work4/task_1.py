# Вычислить число c заданной точностью d
# Пример:

# при $d = 0.001, π = 3.141

from math import pi

accuracy = int(input('Задайте точность для числа Пи: '))

result = round(pi, accuracy)

print(f'Число Пи с заданной точностью {accuracy} = {result}')