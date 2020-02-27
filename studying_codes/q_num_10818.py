n = int(input())

lists = map(int, input().split())
lists_2 = list(lists)

lists_2.sort()

max_num = int(lists_2[n-1])
min_num = int(lists_2[0])
