a = int(input("Enter a value: ")) # a= 5

k = 1

for i in range(1, a+1):  # 1,2,3,4,5
    print(" "*(a-i), end="")# 5-1=4, ba a-i=4
    for j in range(1, k+1):
        print("*", end="")
    print()
    k = k+2
