#다른 진법의 숫자를 10진법으로 변환하는 함수

# 1001 -> 9  (2진법 1001 을 십진법 9)

def convert_to_decimal(number:int, base:int):
    mult, result = 1, 0
    while number >0:
        result += number % 10 *mult
        mult *= base
        number = number // 10
    
    return result


def test_convert_to_decimal():
    number , base = 1001, 2
    try:
        assert(convert_to_decimal(number,base) == 9 )
        print("test complete")
    except Exception as e:
        print("error occur {}".format(e))



if __name__ == "__main__":
    test_convert_to_decimal()



    


    