a = int(input("Enter a value: "))

for i in range(0,a):
    print(" "*(a-i-1),end="")
    for j in range(0,i+1):
        print(j+1, end="")
    print()

a = int(input("Enter a value: "))

for i in range(0,a):
    print(" "*(a-i-1),end="")
    for j in range(0,i+1):
        print(i+1, end="")
    print()
