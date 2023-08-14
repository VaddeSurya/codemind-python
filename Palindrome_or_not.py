string = input()
string = string.lower()
string = string.replace(" ", "")
if string == string[::-1]:
    print("True")
else:
    print("False")
