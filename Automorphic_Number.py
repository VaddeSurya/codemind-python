def automorphic(number):
    square = number ** 2
    num_dig = len(str(number))
    return str(square)[-num_dig:] == str(number)
num = int(input())
if automorphic(num):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")
