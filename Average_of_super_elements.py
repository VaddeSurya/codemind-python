N = int(input())
array = list(map(int, input().split()))
element_count = {}
for num in array:
    if num in element_count:
        element_count[num] += 1
    else:
        element_count[num] = 1
sum_satisfying = 0
count_satisfying = 0
for num, count in element_count.items():
    if num == count:
        sum_satisfying += num
        count_satisfying += 1
if count_satisfying > 0:
    average = sum_satisfying / count_satisfying
    print("{:.2f}".format(average))
else:
    print(-1)
