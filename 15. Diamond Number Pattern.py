a = int(input("Enter a value: "))

for i in range(1, a+1):  #1,2,3,4,5
    print(" "*(a-i), end="") #a-i ba 5-1= 4
    for j in range(1, i+1): #1,2=1 
        print(i, end=" ")
    print()

for i in range((a-1), 0,-1): # 4,3,2,1
    print(" "*(a-i),end="") # (5-4)=1
    for j in range(1, i+1): # 1,2,3,4
        print(i, end=" ")
    print()


a = int(input("Enter a value: "))

for i in range(1, a+1):  #1,2,3,4,5
    print(" "*(a-i), end="") #a-i ba 5-1= 4
    for j in range(1, i+1): #1,2=1 
        print(j, end=" ") # j = 1,2,3,4,
    print()

for i in range((a-1), 0,-1): # 4,3,2,1
    print(" "*(a-i),end="") # (5-4)=1
    for j in range(1, i+1): # 1,2,3,4
        print(j, end=" ")# j = 1,2,3,4,
    print()
