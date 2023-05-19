N = int(input())
array = list(map(int, input().split()))
element_count = {}
for num in array:
    if num in element_count:
        element_count[num] += 1
    else:
        element_count[num] = 1
count_satisfying = 0
for num, count in element_count.items():
    if num == count:
        count_satisfying += 1
print(count_satisfying)
