import math

#에라토스테네스의 체

# 1에서 1000까지의 수중 소수 찾아보기

def make_prime_table():
    array = [ True for i in range(1000001)]
    array[1] = 0
    result = []
    for i in range(2, int(math.sqrt(1000001)) +1):
        if array[i] == True:
            j = 2
            while i * j <= 1000000:
                array[i * j] = False
                j += 1

    for i in range(1, 1000001):
        if array[i]:
            result.append(i)
    
    return result


if __name__ == "__main__":
    prime_table = make_prime_table()
    #print(prime_table)
    #M = int(input())
    #N = int(input())
    M, N = map(int, input().split(' '))
    range_table = [x for x in prime_table if N >= x >= M]
    for value in range_table:
        print(value)

    
   