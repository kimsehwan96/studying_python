import math

#에라토스테네스의 체

# 1에서 1000까지의 수중 소수 찾아보기

def make_prime_table():
    array = [ True for i in range(10001)]
    array[1] = 0
    result = []
    for i in range(2, int(math.sqrt(10001)) +1):
        if array[i] == True:
            j = 2
            while i * j <= 10000:
                array[i * j] = False
                j += 1

    for i in range(1, 10001):
        if array[i]:
            result.append(i)
    
    return result


if __name__ == "__main__":
    prime_table = make_prime_table()
    #print(prime_table)
    M = int(input())
    N = int(input())
    range_table = [x for x in prime_table if N >= x >= M]
    sum = 0
    for value in range_table:
        sum += value
    try:
        minimum = range_table[0]
    except IndexError:
        pass
    if not range_table:
        print('-1')
    else:
        print(sum)
        print(minimum)
    
   