import math

def isPerfectSquare(num):
    sq = int(math.sqrt(num))
    return sq * sq == num

def isFibonacci(num):
    return isPerfectSquare(5*num*num + 4) or isPerfectSquare(5*num*num - 4)

n = int(input())

if isFibonacci(n):
    print("True")
else:
    print("False")