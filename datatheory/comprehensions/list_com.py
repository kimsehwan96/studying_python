
def sqr_1():
    squares = []
    for x in range(10):
        squares.append(x**2)
    #print(squares)

#위 코드는 x라는 이름의 변수를 만들거나 오버라이딩하고, 루프가 종료된 이후에도 남아있는다.

def sqr_2():
    squares = list(map(lambda x: x**2, range(10)))
    #print(squares)

def sqr_3():
    squares = [x**2 for x in range(10)]
    #print(squares)

#위 코드는 매우 깔끔하게 x라는 이름의 변수를 루프 종료 이후에 남겨놓지 않고 처리한다.
#map(함수, 이터러블객체) -> 함수에 이터러블한 객체를 순차적으로 넣는다. 

if __name__ == "__main__":
    import timeit
    t1 = timeit.Timer("sqr_1()", "from __main__ import sqr_1")
    print("sqr1 {} ".format(t1.timeit(number = 10000)))
    t2 = timeit.Timer("sqr_2()", "from __main__ import sqr_2")
    print("sqr2 {} ".format(t2.timeit(number = 10000)))
    t3 = timeit.Timer("sqr_3()", "from __main__ import sqr_3")
    print("sqr3 {} ".format(t3.timeit(number = 10000)))

    #sqr_3 이 가장 좋은 성능을 발휘함.
