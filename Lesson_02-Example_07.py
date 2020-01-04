i = 0
x = 0
data = []

number = int(input())
while number > 0:
    data.insert(0, number % 10)
    i += 1
    number = number // 10

number = 1
for x in range(i):
    number *= data[x]
print(number)

"""
Задача 7.
Найти произведение цифр числа.
"""