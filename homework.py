# Task № 1

#  Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# Пример:
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# n = int(input("Enter number: "))
# dictionary = {}
# for i in range(1, n+1):
#     dictionary[i] = (3*i)+1
# print(dictionary)


# Task № 2
# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# n = int(input("Enter number: "))
# factorial_list = []
# factorial = 1
# for i in range(1, n+1):
#     if (n > 0):
#         factorial = (i * factorial)
#         factorial_list.append(factorial)
# print(factorial_list)


#  Task № 3
# Задайте список из n чисел последовательности (1+ (1/n))^n и выведите на экран их сумму.
# Пример:
# Для n = 5: сумма = 11,55

# n = int(input('Enter number: '))
# n_list = []
# amount = 0
# for i in range(0,n+1):
#     n_list.append((1+(1/n))**n)
#     amount = amount + n_list[i]
# print(amount)


#  Task № 4
#  Задайте число N и создайте список, заполненный числами из промежутка [-N, N].
#  Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.


# n_list = []
# negative_n = int(input('Enter minimal number: '))
# positive_n = int(input('Enter maximal number: '))
# amount = 0
# data = open('file.txt', 'w')
# for i in range(negative_n, positive_n+1):
#     amount = i * (i + 1) + amount
#     data.write(str(amount) + '\n')
#     n_list.append(i)
#     print(n_list)
#     print(amount)


# data.close()

# Task № 5
# Реализуйте алгоритм перемешивания списка.(Без использования библиотеки random)


# import datetime
# input_list = [12,1,34,234,2,56]
# random_list = []
# for i in range(len(input_list)):
#   random_list.append(datetime.datetime.now().microsecond * input_list[i] % 100)
# print(random_list)
  