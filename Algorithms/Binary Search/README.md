# 이진탐색

## 이진탐색이란?
`오름차순으로 정렬된 배열에서 원하는 숫자를 찾는 알고리즘`
* 1. 배열 전체의 중간값을 target 값과 비교
* 2. 중간값이 target 값보다 크면 왼쪽부분만 선택
* 3. 왼쪽부분의 중간값을 다시 target과 비교

## 두가지 방법

* 1. 정방향으로 푸는 방법
* 2. 재귀로 푸는 방법

`[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]`
위와 같은 배열에서 배열의 중간을 잘라서, 중간값보다 Target이 작으면 왼쪽부분만 비교한다. (이걸 반복)

```python3
target = 25
m_list = [30, 94, 27, 92, 21, 37, 25, 47, 25, 53, 98, 19, 32, 32, 7]
length = len(m_list)

m_list.sort()
left = 0 
right = length-1

while left<=right:
    mid = (left+right)//2
    if m_list[mid] == target:
        print(mid+1)
        break
    elif m_list[mid]>target:
        right = mid-1
    else :
        left = mid+1
```