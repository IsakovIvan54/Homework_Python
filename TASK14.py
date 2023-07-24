# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.


pows = int(input('Введите N: '))

count = 0
result = 0
result = pow(2, 0)

while result < pows:
    count += 1
    print(result)
    result = pow(2, count)

    

