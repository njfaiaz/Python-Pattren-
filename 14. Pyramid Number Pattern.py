a = int(input("Enter a value: ")) # a= 5

k = 1

for i in range(1, a+1):  # 1,2,3,4,5
    print(" "*(a-i), end="")# 5-1=4, ba a-i=4
    for j in range(1, k+1): # k = 2 ->1
        print(i, end="")
    print()
    k = k+2

a = int(input("Enter a value: ")) # a= 5

k = 1
p = 1
for i in range(1, a+1):  # 1,2,3,4,5
    print(" "*(a-i), end="")# 5-1=4, ba a-i=4
    for j in range(1, k+1): # k = 2 ->1
        print(p, end="")
    print()
    k = k+2
    p = p+2
