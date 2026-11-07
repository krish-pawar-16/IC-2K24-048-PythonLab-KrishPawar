# Print right angle triangle

n = int(input("Enter value: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()