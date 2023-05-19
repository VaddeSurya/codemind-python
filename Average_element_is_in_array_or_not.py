n = int(input())
array = list(map(int, input().split()))
total = sum(array)
average = total // n 
result = average in array
print(result)
