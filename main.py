import math #Подключение библиотеки math

num = input("Введите вещественные числа в список: ") #Ввод чисел для списка с клавиатуры
a = [float(i) for i in num.split()] #Добавление чисел в список
b = [math.floor(i) for i in a] #Генератор списка принимающий список вещественных чисел и округляющий их до целых 
print("Список целых частей ваших чисел: ", b) #Вывод преобразованного списка на консоль
