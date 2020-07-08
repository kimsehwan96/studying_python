import re

# 보통은 이렇게 사용한다고 한다.

p = re.compile('[a-zA-z]e.lo')
m = p.match("hello world")

if m:
    print("match found :", m.group())
else:
    print("no match")