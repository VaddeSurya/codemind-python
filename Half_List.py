n = int(input()) 
arr = list(map(int, input().split()))
mid = len(arr) // 2  
first = arr[mid:][::-1]  
second = arr[:mid]  
result = first + second
for num in result:
    print(num, end=' ')
