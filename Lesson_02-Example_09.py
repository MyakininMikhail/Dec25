data = []
number = int(input())

while number > 0:
    data.insert(0, number % 10)
    number = number // 10
print(max(data))

"""
Задача 9
Найти максимальную цифру в числе
"""
