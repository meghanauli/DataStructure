n = 4

for row in range(1,2*n + 1):
    c = 2*n-row if row > n else row
    print(c)

    for space in range(n-c):
        print(" ",end="")
    for cols in range(c,0,-1):
        print(cols,end="")
    for cols in range(2,c+1):
        print(cols,end="")
    print()