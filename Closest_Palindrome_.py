def is_palindrome(n):
    return str(n) == str(n)[::-1]
n = int(input())
greater = n + 1
while not is_palindrome(greater):
    greater += 1
smaller = n - 1
while not is_palindrome(smaller):
    smaller -= 1
diff_greater = abs(greater - n)
diff_smaller = abs(smaller - n)
if diff_greater < diff_smaller:
    print(greater)
elif diff_smaller < diff_greater:
    print(smaller)
else:
    print(smaller, greater)
