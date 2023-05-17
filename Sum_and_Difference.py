num1, num2 = map(int, input().split())
num3, num4 = map(float, input().split())

sum_int = num1 + num2
diff_int = num1 - num2

sum_float = num3 + num4
diff_float = num3 - num4

print(sum_int, diff_int)
print("{:.1f} {:.1f}".format(sum_float, diff_float))
