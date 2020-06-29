
def test(a, *args, **kwargs):
    print("this is first arg a {}".format(a))
    for i in args:
        print(i)
    print("-"*40)
    for kw in kwargs:
        print(kw, ":", kwargs[kw])

# 위 함수는 a 라는 위치인자를 하나 무조건 받아야 하고, 추가적인 인자들은 *args로 받음, 키워드 인자들은 **kwargs로 받는다.

if __name__== "__main__":
    test("this is a", "first args", "second args","third args", firstkwarg="first", secondkwargs = "second")