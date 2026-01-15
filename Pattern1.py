n = 5

for i in range(1, n + 1):
    # spaces for alignment
    print("  " * (n - i), end="")

    # descending part
    for j in range(i, 0, -1):
        print(j, end=" ")

    # ascending part
    for j in range(2, i + 1):
        print(j, end=" ")

    print()
