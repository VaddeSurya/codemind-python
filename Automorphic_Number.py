num = int(input())
square = num ** 2
num_dig = len(str(num))

if str(square)[-num_dig:] == str(num):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")
