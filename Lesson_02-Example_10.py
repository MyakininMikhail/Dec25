i = 0
number = int(input())
while number > 0:
    if number % 10 == 5:
        i += 1
    number = number // 10

print(i)

"""
Задача 10.
Найти количество цифр 5 в числе
"""