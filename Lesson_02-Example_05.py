i = 0
x = 0
data = []
number = int(input())

while number > 0:
    data.insert(0, number % 10)
    i += 1
    number = number // 10

for x in range(i):
    print(data[x])

"""
Задача 5.
Вывести цифры числа на каждой строчке.
"""
