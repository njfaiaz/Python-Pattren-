a = int(input("Enter a value: "))
for i in range(a, 0, -1):
    for j in range(0, i):
        print("* ", end=(""))
    print()
