i = 0
x = 0
data = []

number = int(input())
while number > 0:
    data.insert(0, number % 10)
    i += 1
    x += number % 10
    number = number // 10
print(x)

"""
Задача 6
Найти сумму цифр числа.
"""