n, m = map(int, input().split())  
a = list(map(int, input().split()))  # Array a
b = list(map(int, input().split()))  # Array b
uncommon_elements = [x for x in a + b if (x not in a) or (x not in b)]
print(*uncommon_elements)
