# Задайте список из k чисел последовательности (1 + 1\k)^k и выведите на экран их сумму.

k = int(input("Введите число k: "))
lst = []
s = 0
for i in range(1,k+1):
    s += round((1+1/i)**i, 2)
    lst.append(s)
print(f"Полученная сумма последовательности {lst} равнна {round(s,2)}")

# новый код

lst = [round((1+1/i)**i, 2) for i in range(1,k+1)] # использовал list comprehension
print(f"Полученная сумма последовательности {lst} равнна {round(sum(lst),2)}")