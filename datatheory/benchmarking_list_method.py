def test1():
    l = []
    for i in range(1000):
        l = l + [i]

def test2():
    l = []
    for i in range(1000):
        l.append(i)

def test3():
    l = [i for i in range(1000)]

def test4():
    l = list(range(1000))

if __name__ == "__main__":
    import timeit
    t1 = timeit.Timer("test1()", "from __main__ import test1")
    print("concat", t1.timeit(number=1000), "ms")
    t2 =timeit.Timer("test2()", "from __main__ import test2")
    print("append", t2.timeit(number=1000), "ms")
    t3 = timeit.Timer("test3()", "from __main__ import test3")
    print("Comprehenssion", t3.timeit(number = 1000), "ms")
    t4 = timeit.Timer("test4()", "from __main__ import test4")
    print("list range", t4.timeit(number = 1000), "ms")


# usage of Timer 

# timeit.Timer ("function_name", "position of function -ex : bulit-in-method")

"""
리스트 메서드의 시간 복잡도.

인덱스 [] 접근, 인덱스 할당, append, pop : O(1)
pop(i), insert, del, 삽입, 멤버십 테스트 in : O(n)

sort : O(n log n)
"""