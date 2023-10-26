# Задание 1
def is_palindrome(string):
    string = string.lower() # приводим строку к нижнему регистру
    string = string.replace(" ", "") # удаляем пробелы из строки
    string = string.replace(",", "") # удаляем запятые из строки
    string = string.replace(".", "") # удаляем точки из строки
    reversed_string = string[::-1] # переворачиваем строку
    if string == reversed_string:
        return True
    else:
        return False

string = input("Введите строку: ")
if is_palindrome(string):
    print("Строка является палиндромом")
else:
    print("Строка не является палиндромом")
# Задание 2
text = input()
words = input().split()
for word in words:
    text = text.replace(word, word.upper())
print(text)
# Задание 3
s = input()
print(sum(s.count(x) for x in ('.!?')))
