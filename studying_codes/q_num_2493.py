import sys
# 스택을 두개를 쓰면 되지 않을까라는 생각이 든다.

# class Node:
#     def __init__(self):
#         self.next = None
#         self.data = None
    

# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.Top = None

#     def push(self, data):
#         if self.size == 0:
#             self.Top = Node()
#             self.Top.data =data
#             self.size += 1
#         else:
#             new_node = Node()
#             new_node.data = data 
#             new_node.next = self.Top
#             self.Top = new_node
#             self.size += 1

#     def pop(self):
#         if self.size == 0:
#             return -1
#         else:
#             ret = self.Top.data
#             self.Top = self.Top.next
#             self.size -=1
#             return ret


# 아 속았다
# 파이썬 list의 append와 pop메서드는 시간복잡도가 O(1)이다.
# 스택을 굳이 구현할 필요가 없음

if __name__ =="__main__":
    tc = int(input())
    top = list(map(int, sys.stdin.readline().split())) #공백으로 분리
    s = []
    result = [0] * tc

    for i in range(tc):
        t = top[i]
        while s and top[s[-1]] < t:
            s.pop()
        if s:
            result[i] = s[-1] + 1
        s.append(i)

    print(' '.join(list(map(str, result))))

# 스택을 계속해서 비웠다가 다시 채우고 결과값에 저장하는 로직 생각하는게 많이 어렵다.
# 이 문제는 O(N) 시간 복잡도 로직만 통과 가능하다.
# 스택 문제인줄 알고 하려했더니 DP개념도 어느정도 있는듯
# 지금 보는 탑의 왼쪽 탑이 작다면 저장하지 않아야 O(N) 보장이 가능한듯?
# 하기싫다,,