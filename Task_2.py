# Модульность

# import Modul_1

# print(Modul_1.max_1(5, 9))  # 9

# from Modul_1 import max_1

# print(max_1(5, 9))  # 9


# from Modul_1 import *   # Звездочка означает что из Modul_1 мы импортируем все функции.

# print(max_1(10, 9))  # 10


# import Modul_1

# print(Modul_1.max_1(10, 9))  # 10


import Modul_1 as m1

print(m1.max_1(10, 9))  # 10