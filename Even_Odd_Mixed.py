number = input()

has_even = False
has_odd = False

for digit in number:
    if int(digit) % 2 == 0:
        has_even = True
    else:
        has_odd = True

if has_even and has_odd:
    print("Mixed")
elif has_even:
    print("Even")
else:
    print("Odd")
