n = int(input())
array = list(map(int, input().split()))

odd_elements = []
even_elements = []

for num in array:
    if num % 2 == 0:
        even_elements.append(num)
    else:
        odd_elements.append(num)

for num in odd_elements:
    print(num, end=' ')

for num in even_elements:
    print(num, end=' ')
