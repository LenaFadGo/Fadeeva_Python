from gettext import find

# Задание 1
# 1)
# text = "cегодня у меня дополнительное занятие. cегодня среда."
# i = text.split(". ")
# capitalized_i = [x.capitalize() for x in i]
# result = '. '.join(capitalized_i)
# print(result)

#2)
# text = "cегодня у меня 1 дополнительное занятие. cегодня среда 03 12 2025."
# i = text.split(". ")
# counter = 0
# for b in text:
#     if b.isdigit():
#         counter += 1
# print(counter)

#3)
text = "Cегодня у меня 1 дополнительное занятие! Cегодня среда 03 12 2025!"
counter = 0
for b in text:
    if b == ("!"):
        counter += 1
print(counter)

# Задание 2