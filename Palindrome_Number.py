t = int(input())
for _ in range(t):
    num = int(input())
    original_num = num
    reverse_num = 0
    while num > 0:
        digit = num % 10
        reverse_num = reverse_num * 10 + digit
        num //= 10

    if original_num == reverse_num:
        print("True")
    else:
        print("False")
