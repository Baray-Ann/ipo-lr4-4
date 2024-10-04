import math
a=list(map(float, input("Введите вещественные числа в список: ").split()))
print("Ваш список: ", a)
b=[math.floor(i) for i in a]
print("Список целых частей ваших чисел: ", b)