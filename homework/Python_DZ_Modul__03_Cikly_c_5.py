print("Выберите букву из списка:")
print("a")
print("б")
print("в")
print("г")
print("д")

choice = input("Ваш выбор: ")
if choice == "а":
    n = 6
    for i in range(n):
        print(' ' * (n - i - 1) + '*' * (i + 1))
elif choice == "б":
    n = 6
    for i in range(n):
        print('*' * (i+1) + ((n - i) * ' '))


