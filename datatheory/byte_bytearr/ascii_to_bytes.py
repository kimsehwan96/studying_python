

#1

str = "hello world"
the_bytes_array = bytearray([ord(i) for i in str])
print(the_bytes_array)
print(bytearray([ord(i) for i in str]))


def asc_to_binar(string):
    return bytes([ord(i) for i in string])



print(asc_to_binar("hello"))