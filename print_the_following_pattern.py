N = int(input())

for i in range(N):
    for j in range(N):
        if i == j or i+j == N-1:
            print('x', end='')
        else:
            print('0', end='')
    print()
