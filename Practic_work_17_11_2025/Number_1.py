# Задание 1
import re

# input_string = input("Введите строку: ")
# reversed_string = input_string [::-1]
# print("Слово наоборот: ", reversed_string)

# Задание 2

# string = input("Введите строку: ")
# letters = 0
# numbers = 0
# for char in string:
#     if char.isalpha():
#         letters+=1
#     elif char.isalnum():
#         numbers+=1
# print(f"Букв:{letters}")
# print(f"Цифр:{numbers}")

# Задание 3

# text = input("Ввести текст: ")
# text2 = input("Введите один символ: ")
# if len(text2) != 1:
#     print("Введено более одного символа")
# else:
#     val = text.count(text2)
#     print(f"Символ {text2} встречается в строке {val} раз")

# Задание 4

# text = input("Ввести текст: ")
# x = input("Введите слово для поиска: ")
# count_word = text.count(x)
# val = ""
# my_list = []
# for i in text:
#     if i == " " or i == ",":
#         my_list.append(val)
#         val = ""
#         continue
#     else:
#         string = val+i
#         val = string
# words_counter = 0
# for i in my_list:
#     if i == x:
#         words_counter +=1
# print(count_word)

# Задание 5

text1 = input("Введите текст: ")
letter = input("Введите слово для поиска: ")
replacement = input("Введите слово для замены: ")
new_text = text1.replace(letter, replacement)
print(new_text)
