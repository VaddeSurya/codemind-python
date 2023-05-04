n = int(input())

for i in range(n):
    row = ""
    for j in range(n):
        if i >= j:
            row += str(n-j) + " "
        else:
            row += str(n-i) + " "
    for j in range(n-2, -1, -1):
        if i >= j:
            row += str(n-j) + " "
        else:
            row += str(n-i) + " "
    print(row)
for i in range(n-2, -1, -1):
    row = ""
    for j in range(n):
        if i >= j:
            row += str(n-j) + " "
        else:
            row += str(n-i) + " "
    for j in range(n-2, -1, -1):
        if i >= j:
            row += str(n-j) + " "
        else:
            row += str(n-i) + " "
    print(row)
