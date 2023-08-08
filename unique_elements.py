n = int(input())
arr = list(map(int, input().split()))
arr1 = []
for i in arr:
    if i not in arr1:
        arr1.append(i)
output_str = ' '.join(map(str, arr1))
print(output_str)
