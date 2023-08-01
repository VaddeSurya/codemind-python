import math
size_of_array = int(input())
array = list(map(int, input().split()))

if len(array) != size_of_array:
    print("Error")
else:
    hcf = array[0]
    for num in array[1:]:
        hcf = math.gcd(hcf, num)
    print(hcf)
