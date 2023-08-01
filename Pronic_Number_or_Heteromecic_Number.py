num_input = int(input())
is_pronic = False
for n in range(int(num_input ** 0.5) + 1):
    if n * (n + 1) == num_input:
        is_pronic = True
        break
    
if is_pronic:
    print("YES")
else:
    print("NO")

