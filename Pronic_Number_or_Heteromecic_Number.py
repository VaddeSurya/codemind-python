def is_pronic_number(number):
    for n in range(int(number ** 0.5) + 1):
        if n * (n + 1) == number:
            return True
    return False
num_input = int(input())
if is_pronic_number(num_input):
    print("YES")
else:
    print("NO")

