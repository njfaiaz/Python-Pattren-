a = int(input("Enter a value: "))
for i in range(1, a + 1):
    if i%2 != 0: # odd number print 
        for j in range(1, i+1):
            print("* ", end=(""))
    print()
