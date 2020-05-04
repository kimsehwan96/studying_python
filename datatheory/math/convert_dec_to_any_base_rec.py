#재귀함수를 이용한 진법 변환
# 진법 변환은 number와 base(진법)을 인자로 받는다.
# number 가 진법의 수보다 낮으면 그대로 반환하면 되고
# number가 진법의 수보다 크다면, number를 진법으로 나눈 나머지 -> digit 이 될 것이다. converString 문자표에서 대치하면 된다.
# 그리고 number를 진법으로 나눈 몫을 다시 number로 치환한다. 이 과정을 반복한다. 언제까지? number < base 일 때 까지
def convert_dec_to_any_base_rec(number, base):
    convertString = "0123456789ABCDEF"
    if number < base:
        return convertString[number]
    else:
        return convert_dec_to_any_base_rec(number // base, base) + convertString[number % base]

def test():
    number = 9
    base = 2
    assert(convert_dec_to_any_base_rec(number, base) == '1001')
    print("통과")


if __name__ == "__main__":
    test()