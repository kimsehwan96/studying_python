from util import print_text

ENCODING_TYPE= 'utf-8'

print_text('Hello',ENCODING_TYPE)
print_text('안녕하세요',ENCODING_TYPE)

# utf-8에서 ascii 코드는 각 문자당 1바이트로 완벽하게 매칭 된다 
# utf-8에서 1바이트만 쓰는 경우는 0xxxxxxx 로, x에만 비트가 채워지니까 0~127이 커버가 되므로 ascii 완벽호환
# utf-8에서 한글은 3바이트까지 써야 표현이 되고 4바이트부터는 emoji가 표현이 된다.

print_text("😀😁😂🤣😃😄😅😆😉😊😋😎😍😘🥰",ENCODING_TYPE)

# emoji는 4바이트씩 쓴걸 확인이 가능하다..
# 한자는 3바이트일까?


print_text("漢韓辭典",ENCODING_TYPE)

#한자도 3바이트다!