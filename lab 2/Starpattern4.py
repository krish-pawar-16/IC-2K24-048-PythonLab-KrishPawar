# Square pattern

n = int(input("Enter value:"))

for i in range(1, n + 1):
    if i == 1 or i == n:
        for j in range(1, n + 1):
            print("*", end="")
    else:
        print("*", end="")
        for j in range(1, n - 1):
            print(" ", end="")
        print("*", end="")
    print()