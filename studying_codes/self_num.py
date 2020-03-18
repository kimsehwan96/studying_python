
def d(n):
    """ 셀프넘버 구현 함수 자릿수는 입력을 스트링으로 변환
    길이를 확인함 """

    num = str(n)
    digit = len(num)
    new_number = 0

    for x in range(digit):
        new_number += int(num[x])
    new_number += n

    return new_number


#print(d(100))
lists = []
lists.clear()
for x in range(10000):
    lists.append(d(x))
lists.sort()
#print(lists)

self_num_lists = []

for x in range(10000):
    if lists.count(x) == 0:
        self_num_lists.append(x)
    else:
        pass


for x in range(len(self_num_lists)):
    print(self_num_lists[x])
