a = int(input("Enter a value: ")) #a = 5

for i in range(1,a+1): # 1,2,3,4,5
    for j in range(1, i+1):
        print("*", end="")
    print()

for i in range((a-1),0, -1):
    for j in range(1,i+1):
        print("*", end="")
    print()



b = int(input("Enter a value: "))

for i in range(1,b+1):
    print("*"*i)

for j in range((b-1),0, -1):
    print("*"*j)
