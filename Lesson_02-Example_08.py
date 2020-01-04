number = int(input())
while number > 0:
    if number % 10 == 5:
        print("Yes")
        break
    number = number // 10
else:
    print("No")

"""
Задача 8.
Дать ответ на вопрос: есть ли среди цифр числа 5 ?
"""