a = int(input("Enter a value: "))

for i in range(a+1,1,-1):
    for j in range(1, i):
        print(j, end="")
    print()


a = int(input("Enter a value: "))

for i in range(a+1,1,-1):
    print(" "*(a+1-i), end="")
    for j in range(1, i):
        print(j, end="")
    print()
