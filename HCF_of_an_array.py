import math
def find(arr):
    hcf = arr[0]
    for num in arr[1:]:
        hcf = math.gcd(hcf, num)
    return hcf
size = int(input())
array = list(map(int, input().split()))

if len(array) != size:
    print("Error")
else:
    result = find(array)
    print(result)
