
def print_text(text, encoding_type):
    byte_data = text.encode(encoding_type)
    hex_data_as_str = ' '.join("{}".format(hex(c)) for c in byte_data)
    int_data_as_str = ' '.join("{}".format(int(c)) for c in byte_data)
    
    print('\'' + text + '\' 문자열 길이 : {}'.format(len(text)))
    print('\'' + text + '\' 전체 문자를 표현하는데 사용한 바이트 수 : {} 바이트 '.format(len(byte_data)))

    print('\'' + text + '\' + 16진수 값 : {}'.format(hex_data_as_str))
    print('\'' + text + '\' + 10진수 값 : {} '.format(int_data_as_str))




print_text('Hello', 'euc-kr')
print_text("안녕하세요",'euc-kr')