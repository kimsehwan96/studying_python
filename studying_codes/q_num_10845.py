import sys
from collections import deque

# deque 사용법

# q = deque()
# q.append(값) -> 값을 큐의 오른쪽으로 쭉 붙인다.
# q.popleft() -> 값을 큐의 왼쪽에서부터 뽑아낸다
# list가 아닌 deque 이용하는 이유
# 맨 왼쪽 원소를 pop하는 메서드가 리스트에서는 O(N) 시간 복잡도를 가지기 때문

def push(num : int, queue: deque) -> None:
    queue.append(num)

def pop(queue: deque) -> None:
    if len(queue) == 0:
        print("-1")
    else:
        print(queue.popleft())

def size(queue: deque):
    print(len(queue))

def empty(queue):
    if len(queue) == 0:
        print("1")
    else:
        print("0")

def front(queue):
    if len(queue) == 0:
        print("-1")
    else:
        print(queue[0])

def back(queue):
    if len(queue) == 0:
        print("-1")
    else:
        print(queue[-1])

if __name__=="__main__":
    q = deque() #큐 생성
    tc = int(sys.stdin.readline().rstrip())

    for _ in range(tc):
        cmd = sys.stdin.readline().rstrip()
        if (cmd.count('push')):
            num = int(cmd.split(' ')[1])
            push(num, q)
        if (cmd == "front"):
            front(q)
        if (cmd == "back"):
            back(q)
        if (cmd == "empty"):
            empty(q)
        if (cmd == "size"):
            size(q)
        if (cmd=="pop"):
            pop(q)