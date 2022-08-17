a = int(input("Enter a value: "))

for i in range(1, a+1):
    for k in range(1, a-i):
        print(" ", end="")
    for j in range(1, i+1):
        print("* ", end="")
    print()
