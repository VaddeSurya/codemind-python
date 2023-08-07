num = int(input())

all_even = True
all_odd = True

while num != 0:
    digit = num % 10
    if digit % 2 == 0:
        all_odd = False
    else:
        all_even = False
    num //= 10

if all_even:
    print("Even")
elif all_odd:
    print("Odd")
else:
    print("Mixed")
