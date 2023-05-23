n = input()
largest = 0
for digit in n:
    if int(digit) > largest:
        largest= int(digit)
print(largest)
