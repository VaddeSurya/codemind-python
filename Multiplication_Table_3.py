n, j, r = map(int, input().split())
for i in range(j, r + 1):
    p = n * i
    print(n, "x", i, "=", p)
