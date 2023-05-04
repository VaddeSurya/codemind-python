N = int(input())

for i in range(N):
    for j in range(N):
        if i == j:
            print("0", end="")
        else:
            print("x", end="")
    print()
