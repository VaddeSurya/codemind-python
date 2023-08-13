num1,num2=map(int,input().split())
max_num = max(num1, num2)
while True:
    if max_num % num1 == 0 and max_num % num2 == 0:
        lcm_result = max_num
        break
    max_num += 1

print(lcm_result)
