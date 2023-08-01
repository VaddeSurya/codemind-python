num = int(input())

sq = num ** 2
tot = 0

for i in str(sq):
    tot +=int(i)

if num == tot:
    print("Neon Number")
else:
    print("Not Neon Number")