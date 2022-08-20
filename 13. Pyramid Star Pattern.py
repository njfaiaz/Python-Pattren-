a = int(input("Enter a value: "))

k = 1

for i in range(1, a+1):
    print(" "*(a-i), end="")
    for j in range(1, k+1):
        print("*", end="")
    print()
    k = k+2
