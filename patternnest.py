n = 5
n = n * 2

for rows in range(1,n,1):
    for cols in range(1,n,1):
        left = cols
        right = n - cols
        up = rows
        down = n - rows
        ateverindex = min(left, right, up, down)
        print(ateverindex,end="")
        
    print()
   
        