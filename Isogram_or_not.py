n=input()
setinput=set()
for i in n:
    if i in setinput:
        print("False")
        break
    setinput.add(i)
else:
    print("True")