number = int(input())

square = number * number
digit = 0

while square > 0:
    digit += square % 10
    square //= 10

if digit == number:
    print("Neon Number")
else:
    print("Not Neon Number")
