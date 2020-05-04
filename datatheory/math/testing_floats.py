from fractions import Fraction

def rounding_floats(number1, places):
    return round(number1, places)

number_1 = 1.25
places = 1

#assert ->가정 설정문. assert(func(a)) == b <- a함수의 리턴값이 b가 맞는지 체크, 아닐경우 assertion error 발생. 
assert(rounding_floats(number_1,places) == 1.5)