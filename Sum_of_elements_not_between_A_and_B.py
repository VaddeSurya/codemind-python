n = int(input())
array = list(map(int, input().split()))
a, b = map(int, input().split())

sum_of_elements = 0

for num in array:
    if num < a or num > b:
        sum_of_elements += num

print(sum_of_elements)
