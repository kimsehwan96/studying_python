def conver_from_decimal_lager_bases(number, base):
    strings = '0123456789ABCDEFGHIJ'
    result = ""
    while number > 0:
        digit = number % base
        result = strings[digit] + result
        number = number // base
    return result 