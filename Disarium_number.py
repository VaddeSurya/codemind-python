num = input()  
n = len(num)   
sum = 0

for i in range(n):
    sum += int(num[i])**(i+1)

if sum == int(num):
    print("True")
else:
    print("False")
