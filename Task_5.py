# Алгоритмы
# Быстрая сортировка:
def quicksort(array):  # Определение функции с названием quicksort, которая принимает массив в качестве входного аргумента

    if len(array) <= 1:  # Если длина массива меньше или равна 1, возвращаем массив, так как он уже отсортирован
        return array
    
    else:  # Если длина массива больше 1, выполняем следующие шаги
        pivot = array[0]  # Устанавливаем опорный элемент как первый элемент массива
        less = [i for i in array[1:] if i <= pivot]  # Создаем новый список, содержащий элементы из массива, 
        # которые меньше или равны опорному элементу
        
        greater = [i for i in array[1:] if i > pivot]  # Создаем новый список, содержащий элементы из массива, 
        # которые больше опорного элемента
        return quicksort(less) + [pivot] + quicksort(greater)  # Рекурсивно вызываем функцию quicksort 
    # для списков 'less' и 'greater', а затем объединяем результаты с опорным элементом посередине

print(quicksort([10, 5, 2, 3]))  # Вызываем функцию quicksort с заданным массивом и выводим отсортированный результат



# Быстрая сортировка:
# def quicksort(array): 

#     if len(array) <= 1:
#         return array
    
#     else:
#         pivot = array[0]
#         less = [i for i in array[1:] if i <= pivot]

#         greater = [i for i in array[1:] if i > pivot]
#         return quicksort(less) + [pivot] + quicksort(greater)

# print(quicksort([10, 5, 2, 3]))



# Сортировка слиянием
# def merge_sort(nums):
#     # Проверяем, что длина списка nums больше 1, чтобы его можно было разделить на две части.
#     if len(nums) > 1:
#         # Находим середину списка.
#         mid = len(nums) // 2
        
#         # Разделяем список на две части: левую и правую.
#         left = nums[:mid]
#         right = nums[mid:]
        
#         # Рекурсивно вызываем функцию merge_sort для левой и правой части списка.
#         merge_sort(left)
#         merge_sort(right)
        
#         # Инициализируем переменные для сравнения элементов из левой и правой частей списка.
#         i = j = k = 0
        
#         # Сравниваем элементы из левой и правой частей списка и объединяем их в отсортированный список nums.
#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 nums[k] = left[i]
#                 i += 1
#             else:
#                 nums[k] = right[j]
#                 j += 1
#             k += 1
        
#         # Если в левой части остались элементы, добавляем их в отсортированный список nums.
#         while i < len(left):
#             nums[k] = left[i]
#             i += 1
#             k += 1
        
#         # Если в правой части остались элементы, добавляем их в отсортированный список nums.
#         while j < len(right):
#             nums[k] = right[j]
#             j += 1
#             k += 1

# # Создаем список list1.
# list1 = [38, 27, 43, 3, 9, 82, 10]

# # Вызываем функцию merge_sort для списка list1.
# merge_sort(list1)

# # Печатаем отсортированный список list1.
# print(list1)



# Сортировка слиянием
# def merge_sort(nums):
#     if len(nums) > 1:
#         mid = len(nums) // 2
#         left = nums[:mid]
#         right = nums[mid:]
#         merge_sort(left)
#         merge_sort(right)
        
#         i = j = k = 0
#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 nums[k] = left[i]
#                 i += 1
#             else:
#                 nums[k] = right[j]
#                 j += 1
#             k += 1
            
#         while i < len(left):
#             nums[k] = left[i]
#             i += 1
#             k += 1
        
#         while j < len(right):
#             nums[k] = right[j]
#             j += 1
#             k += 1

# list1 = [38, 27, 43, 3, 9, 82, 10]
# merge_sort(list1)
# print(list1)
