n = input()
setinput = set()
for i in n:
    if i != " ":
        setinput.add(i.lower())
print("".join(sorted(setinput)))
