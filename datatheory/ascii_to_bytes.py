

#1

str = "hello world"
the_bytes_array = [ord(i) for i in str]
print(the_bytes_array)

def asc_to_binar(string):
    return [ord(i) for i in string]



print(asc_to_binar("hello"))