number = input()
is_unique = True
for digit in number:
    if number.count(digit) > 1:
        is_unique = False
        break
if is_unique:
    print("Unique Number")
else:
    print("Not Unique Number")
