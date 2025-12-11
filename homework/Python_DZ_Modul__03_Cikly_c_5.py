print("Выберите букву из списка:")
print("a")
print("б")
print("в")
print("г")
print("д")

choice = input("Ваш выбор: ")
if choice == "а":
    n = 10
    for i in reversed(range(1,n+1)):
        print(' ' * (n - i), '*' * i)

if choice == "б":
    n = 10
    for i in range(n):
        print('*' * (i + 1) + ((n - i) * ' '))

if choice == "в":
    n = 10
    k = 2 * n - 2
    for i in range(n, -1, -1):
        for j in range(k, 0, -1):
            print(end=" ")
        k = k + 1
        for j in range(0, i):
            print("*", end=" ")
        print("")

if choice == "г":
    n = 10
    for i in range (1,n+1):
        print(" " * n, end='')
        print('* ' * (i))
        n -= 1








