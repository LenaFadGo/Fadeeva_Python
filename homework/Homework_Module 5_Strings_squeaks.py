# Задание 1

string = input("Введите стоку: ")
print(string.replace(" ","").lower() == string[::-1].replace(" ","").lower())

# Задание 2

text = input("Введите текст: ")
reserved_words = input("Введите список зарезервированных слов через пробел: ")
words = text.split()
for x in range(len(words)):
    if words[x] in reserved_words:
        words[x] = words[x].upper()
new_text = ' '.join(words)
print(new_text)

# Задание 3

text = "Сегодня мы на уроке изучали строки и списки. А ранее циклы."
sentences = 0
for char in text:
    if char in ".!?":
        sentences += 1
print(f"Количество предложений {sentences}.")



