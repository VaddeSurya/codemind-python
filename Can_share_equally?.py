x,y=map(int,input().split())
z=(x+(2*y))
if z%2==0 and x%2==0 and y%2==0:
    print("YES")
elif x!=0 and x%2==0:
    print("YES")
elif x==0 and y%2==0:
    print("YES")
else:
    print("NO")