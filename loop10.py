i = 0
s = 1

for i in range(1, 6):
    for s in range(1, 6-i):
        print(" ",end="")
    for s in range(1, 1+i):
        print("*", end="")
    print()
