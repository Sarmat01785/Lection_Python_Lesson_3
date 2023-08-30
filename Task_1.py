"""
Задание: Необходимо создать функцию sumNumbers(n), которая будет считать
сумму всех элементов от 1 до n.
"""

# def sumNumbers(n):
#     summa = 0
#     for i in range(1, n + 1):
#         summa += i
#     print(summa)
    
# sumNumbers(5)


# def sumNumbers(n):
#     summa = 0
#     for i in range(1, n + 1):
#         summa += i
#     return summa
    
# print(sumNumbers(5)) # 15


# def sumNumbers(n):
#     summa = 0
#     for i in range(1, n + 1):
#         summa += i
#     return summa
    
# a = sumNumbers(5)
# print(a)  # 15


# Давайте изменим наш код и добавим в него return. НО перед этим давайте
# вспомним, что делает return:
# 1. Завершает работу функции
# 2. Возвращает значение
# def sumNumbers(n, y =  "Hallo" ):
#     print(y)
#     summa = 0
#     for i in range(1, n + 1):
#         summa += i
#     return summa
    
# a = sumNumbers(5)
# print(a)  # 15


# def sumNumbers(n, y =  "Hallo" ):
#     print(y)  # Привет
#     summa = 0
#     for i in range(1, n + 1):
#         summa += i
#     return summa
    
# a = sumNumbers(5 , "Привет")
# print(a)  # 15

# Спросим у пользователя число:
# def sumNumbers(n):
#     summa = 0
#     for i in range(1, n + 1):
#         summa += i
#     print(summa)
# n = int(input("Введите целое число: ")) # 5
# sumNumbers(n) # 15


# Передача не огранниченного количества аргументов.
# def sum_str(*args):
#     res = " "
#     for _ in args: # for i in args:
#         res += _   # res += i
#     return res
# print(sum_str("П","р", "и", "в", "е", "т"))
# print(sum_str("П","р", "и", "в", "е", "т", "В", "а", "с", "я"))

"""
Возможность передачи неограниченного количества аргументов
● Можно указать любое количество значений аргумента функции.
● Перед аргументом надо поставить *.
В примере ниже функция работает со строкой, поэтому при введении чисел
программа выдаёт ошибку:
"""
def concatenatio(*params):
    res = ""
    for item in params:
        res += item
    return res
print(concatenatio('a', 's', 'd', 'w')) # asdw
print(concatenatio('a', '1')) # a1
# print(concatenatio(1, 2, 3, 4)) # TypeError: ...

        