import math

#에라토스테네스의 체

# 1에서 1000까지의 수중 소수 찾아보기

def make_prime_table():
    array = [ True for i in range(1001)]
    array[1] = 0
    result = []
    for i in range(2, int(math.sqrt(1001)) +1):
        if array[i] == True:
            j = 2
            while i * j <= 1000:
                array[i * j] = False
                j += 1

    for i in range(1, 1001):
        if array[i]:
            result.append(i)
    
    return result


if __name__ == "__main__":
    prime_table = make_prime_table()
    count = 0
    num = int(input())
    nums = list(map(int, input().split(' ')))
    for values in nums:
        if values in prime_table:
            count += 1
        else:
            pass
    
    print(count)
