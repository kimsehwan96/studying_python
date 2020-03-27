import struct
import sys

var = struct.pack('iii',1,2,3)

print(var)
print(type(var))
print("byte order of this sys is: ", sys.byteorder)

unvar = struct.unpack('iii', var)
print("result of unpack var : ", unvar)


print("------------------------------------------------")

print(var)
print("length of var is", len(var), 'bytes')

# x01\x00\x00\x00 <- 이건 1을 의미
# x02\x00\x00\x00 <- 이건 2를 의미.

#unpack 하면 튜플 형태로 저장된다.

# usage of pack : pack(character format , *args_)

test_8bitint = struct.pack('qqq',1,5,10)
print(test_8bitint)
print("lenth of long long integers, 3 components:", len(test_8bitint))
print("\n\n")

int_25550 = struct.pack('i',2147483642)
print(int_25550)
print('\n\n')

# python bytes 객체에 대한 remind

#바이트 객체 선언

bt = b'hello'
print(bt)
print(type(bt), len(bt))
# bytes 객체는 바이트 조작이 불가능함
# bt[0] = 2 <- 불가능

print('\n\n')

be = bytearray(b'hello')
print(be)
for x in be:
    print(x)

# bytearray 객체는 iterable 하다.

#  바이트 객체를 문자열로 바꾸기 위해서는 .decode 이용

t = b'hello'.decode('utf-8')

print(t)