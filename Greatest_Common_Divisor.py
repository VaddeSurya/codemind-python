num1,num2=map(int,input().split())

while num2:
    num1, num2 = num2, num1 % num2
hcf = num1
print(hcf)
