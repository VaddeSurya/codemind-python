n=input()
words=n.split()
count=0
for i in words:
    i=i.lower()
    i=i.replace(" ","")
    if i==i[::-1]:
        count+=1
print(count)