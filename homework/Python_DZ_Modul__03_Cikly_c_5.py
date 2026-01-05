print("Выберите букву из списка:")
print("a")
print("б")
print("в")
print("г")
print("д")
print("е")
print("ж")
print("з")
print("и")
print("к")

choice = input("Ваш выбор: ")
if choice == "а":
    n = 6
    for i in reversed(range(1,n+1)):
        print(' ' * (n - i), '*' * i)

if choice == "б":
    n = 6
    for i in range(n):
        print('*' * (i + 1) + ((n - i) * ' '))

if choice == "в":
    n = 6
    k = 2 * n - 2
    for i in range(n, -1, -1):
        for j in range(k, 0, -1):
            print(end=" ")
        k = k + 1
        for j in range(0, i):
            print("*", end=" ")
        print("")

if choice == "г":
    n = 5
    for i in range (1,n+1):
        print(" " * n, end='')
        print('* ' * (i))
        n -= 1

if choice == "д":
    n = 5
    for i in range(n):
        spaces = ' ' * i
        stars = '*' * (2 * (n - i) - 1)
        print(spaces + stars)
    for i in range(1, n):
        spaces = ' ' * (n - i - 1)
        stars = '*' * (2 * i + 1)
        print(spaces + stars)

if choice == "е":
    n=6# ширина в звездах
    for i in range (n):
        stars = "*" * (i+1)
        spaces = ' ' * (2 * (n- i - 1))
        print(stars + spaces + stars)
    for i in range (n-2,-1,-1):
        stars = "*" * (i+1)
        spaces = ' ' * (2 * (n-i-1))
        print(stars + spaces + stars)







