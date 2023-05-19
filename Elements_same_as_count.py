N = int(input())
array = list(map(int, input().split()))
element_count = {}
for num in array:
    if num in element_count:
        element_count[num] += 1
    else:
        element_count[num] = 1
result = [num for num, count in element_count.items() if num == count]
if len(result) > 0:
    print(" ".join(map(str, result)))
else:
    print(-1)
