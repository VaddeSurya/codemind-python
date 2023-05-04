N = int(input())

for i in range(1, N+1):
    spaces = " "*(N-i)
    num = str(i)*((2*i)-1)
    print(spaces+num)
