# Задание 1

import re

# 1)
text_number = [1, 12, 33, 125, 5, 9, 32, -48, -33, -15, 22, 24, 16, 19, 3, 23, 222, 0]
neg_number = 0
even_numbers = 0
not_even_even = 0
a = 0
# for i in text_number:
#     if i < 0:
#         neg_number += i
#     if i // 2:
#         even_numbers += i
#     if i % 2:
#         not_even_even += i
x = len(text_number)
print(x)
for val in range(3, len(text_number), 3):
    a += text_number[val]
print(a)


