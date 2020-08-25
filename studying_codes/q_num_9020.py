import math
import sys

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

def gold_partion(n, table):
    # 인자인 table은 2~10000 까지의 소수가 저장되어있으
    # n은 항상 짝수
    tmp_list = [x for x in table if x < n]
    if (n // 2) in tmp_list:
        print("{} {}".format(n//2, n//2))
    else:
        buf = None
        for idx in range(len(tmp_list)):
            reverse_idx = -(idx+1)
            target = tmp_list[reverse_idx]
            for idx in range(len(tmp_list)):
                result = target + tmp_list[idx]
                if result == n:
                    if buf == None:
                        buf = (target, tmp_list[idx])
                    elif buf[0] == tmp_list[idx]:
                        return print("{} {}".format(target, tmp_list[idx]))
                    else:
                        buf = (target, tmp_list[idx])
                else:
                    pass

if __name__ == "__main__":
    input_list = []
    result = []
    prime_table = make_prime_table()
    #print(prime_table)
    test_case = int(sys.stdin.readline())
    for values in range(test_case):
        input_list.append(int(sys.stdin.readline()))
    for idx in range(len(input_list)):
        gold_partion(input_list[idx], prime_table)

    #gold_partion(10, prime_table)


    
   