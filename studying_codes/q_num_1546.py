


n = int(input())
subject = []
subject.clear()

subject = list(map(int, input().split()))

subject.sort()
M = subject[n-1]

new_list = []
new_list.clear()

for x in range(n):
    new_score = (subject[x] / M)* 100
    new_list.append(new_score)

new_sum = 0

for x in range(n):
    new_sum = new_sum + new_list[x]

print(new_sum/n)
