# Ищем дробные числа

import re
text = "Сегодня я выпил 4 чашки кофе. Вчера было 6. Слово11"
# pattern = re.compile(r"(вчера)", re.IGNORECASE)
float_int = re.compile(r"[+-]?\d+(\.\d+)?")
val = re.search(float_int, text)
print(val.group())

# Поиск почты

import re
text = "Сегодня я выпил 4 чашки кофе. Вчера было 6. Слово11"
# pattern = re.compile(r"(вчера)", re.IGNORECASE)
float_int = re.compile(r"[+-]?\d+(\.\d+)?")
email_pattern= re.compile(r"\w+@\w\.\w+")
val = re.search(float_int, text)
print(val.group())

