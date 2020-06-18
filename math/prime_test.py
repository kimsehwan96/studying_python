import math
import random

def finding_prime(number):
    num = abs(number)
    if num < 4 : return True
    for x in range(2, num):
        if num % x ==0:
            return False
    return True

def finding_prim_sqrt(number):
    num = abs(number)
    if num < 4 : return True
    for x in range(2, int(math.sqrt(num)) +1):
        if number % x ==0:
            return False
    return True


def test_prime():
    number1 = 17
    number2 = 20
    assert(finding_prime(number1) is True)
    assert(finding_prime(number2) is False)
    assert (finding_prim_sqrt(number1) is True)
    assert(finding_prim_sqrt(number2) is False) 
    print("테스트 통과 ")



if __name__ == "__main__":
    test_prime()