import math

#에라토스테네스의 체

# n <= 123456
# 2n = 246912

maximum = 246912

def make_prime_table():
    array = [ True for i in range(maximum+1)]
    array[1] = 0
    result = []
    for i in range(2, int(math.sqrt(maximum+1)) +1):
        if array[i] == True:
            j = 2
            while i * j <= maximum:
                array[i * j] = False
                j += 1

    for i in range(1, maximum+1):
        if array[i]:
            result.append(i)
    
    return result

def gong_jun(n, table):
    checked_table = [x for x in table if 2*n >= x > n]
    #print(checked_table)
    print(len(checked_table))


if __name__ == "__main__":
    prime_table = make_prime_table()
    #print(prime_table)
    stop = True
    test_case = None
    num_list = []
    while True:
        test_case = int(input())
        if test_case == 0:
            break
        else:
            num_list.append(test_case)

    for values in num_list:
        gong_jun(values, prime_table)
        

    #계속 틀린이유... 리스트 조건식에 >이 아닌 >= 이 들어갔네 문제 잘보기 ㅠㅠ
   