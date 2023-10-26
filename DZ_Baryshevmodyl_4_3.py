import random
list1 = [random.randint(-10, 10) for _ in range(10)]
list2 = [random.randint(-10, 10) for _ in range(10)]
merged_list = list1 + list2
unique_merged_list = list(set(merged_list))
common_elements_list = list(set(list1) & set(list2))
unique_elements_list = list(set(list1) ^ set(list2))
min_max_list = [min(list1), max(list1), min(list2), max(list2)]
print("Первый список:", list1)
print("Второй список:", list2)
print("Список, содержащий элементы обоих списков:", merged_list)
print("Список, содержащий элементы обоих списков без повторений:", unique_merged_list)
print("Список, содержащий элементы общие для двух списков:", common_elements_list)
print("Список, содержащий только уникальные элементы каждого из списков:", unique_elements_list)
print("Список, содержащий только минимальное и максимальное значение каждого из списков:", min_max_list)