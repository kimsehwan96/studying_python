list = []
list.clear()

for x in range(10):
    b = int(input())
    list.insert(x,b)
list_result = []
list_result.clear()

for x in range(10):
    b = list[x] % 42
    list_result.insert(x,b)

s = set(list_result)

print(len(s))
