# Задание 1
a = input("Введите арифметическое выражение: ")
result = eval(a)
print("Результат выражения:", result)
# Задание 2
import random
numbers = [random.randint(-10, 10) for i in range(10)]
min_number = min(numbers)
max_number = max(numbers)
negative_count = sum(1 for num in numbers if num < 0)
positive_count = sum(1 for num in numbers if num > 0)
zero_count = sum(1 for num in numbers if num == 0)
print("Список чисел:", numbers)
print("Минимальный элемент:", min_number)
print("Максимальный элемент:", max_number)
print("Количество отрицательных элементов:", negative_count)
print("Количество положительных элементов:", positive_count)
print("Количество нулей:", zero_count)
