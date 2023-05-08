def isPerfectSquare(n):
    if n < 0:
        return False
    root = int(n**0.5)
    return root * root == n
n = int(input())
if isPerfectSquare(n):
    print("True")
else:
    print("False")
