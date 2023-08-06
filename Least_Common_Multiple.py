def compute_gcd(x, y):
   while(y):
       x, y = y, x % y
   return x
def full_lcm(x, y):
   lcm = (x*y)//compute_gcd(x,y)
   return lcm

num1,num2=map(int,input().split())

print(full_lcm(num1, num2))
