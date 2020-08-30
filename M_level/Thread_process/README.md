# 스레드

```python3
from threading import Thread
```

스레딩 모듈을 임포트해서 사용한다. 

멀티 스레드와 멀티 프로세스에 대해서 알아보자

* python 에서 멀티 스레드를 구현하는 방법은 threading(High level) 혹은 thread(Low level)

-> threading 모듈 임포트를 추천한다.

```console
[Running] python -u "/Users/gimsehwan/studying_python/M_level/Thread/first.py"
Result : 4999999950000000

[Done] exited with code=0 in 4.924 seconds

[Running] python -u "/Users/gimsehwan/studying_python/M_level/Thread/multyThread.py"
Result : 4999999950000000

[Done] exited with code=0 in 4.845 seconds
```

스레드 1개로 실행한 결과와, 2개의 스레드로 실행한 결과가 거의 동일하다.

# GIL (Global Interpreter Lock)

    하나의 프로세스 안에 모든 자원의 Lock을 글로벌하게 관리하는 정책.

## 멀티 스레드

```python3

from threading import Thread

def work(id, start, end, result):
    total = 0
    for i in range(start, end):
        total += i
    result.append(total)
    return

if __name__ == "__main__":
    START, END = 0, 100000000
    result = list()
    th1 = Thread(target=work, args=(1, START, END//2, result))
    th2 = Thread(target=work, args=(1, END//2, END, result))

    th1.start()
    th2.start()
    th1.join()
    th2.join()

print(f"Result : {sum(result)}")

```

## 멀티 프로세스

```python3

from multiprocessing import Process, Queue

def work(id, start, end, result):
    total = 0
    for i in range(start, end):
        total += i
    result.put(total)
    return

if __name__ == "__main__":
    START, END = 0, 100000000
    result = Queue()
    th1 = Process(target=work, args=(1, START, END//2, result))
    th2 = Process(target=work, args=(2, END//2, END, result))

    th1.start()
    th2.start()
    th1.join()
    th2.join()

    result.put('STOP')
    total = 0

    while True:
        tmp = result.get()
        if tmp == 'STOP':
            break
        else:
            total += tmp
    
    print(f"result: {total}")

```

멀티 프로세스의 콘솔 결과

```console
[Running] python -u "/Users/gimsehwan/studying_python/M_level/Thread_process/multprocess.py"
result: 4999999950000000

[Done] exited with code=0 in 2.598 seconds
```

2초 정도 더 빨랐따.

## 멀티 프로세스와 스레드의 차이점.

멀티 프로세싱 모듈의 가장 큰 장점은 스레딩 모듈과 구현 방식이 거의 같다.
다만 result로 Queue 객체를 사용 할 뿐이다.  

단점으로는 프로세스는 각자 고유한 메모리 영역을 가지기 때문에 메모리 사용은 늘어난다.

* 각각 프로세스가 자신만의 메모리 공간을 사용하기 때문에 
* 프로세스간 데이터 교환을 위해 multiprocessing.Queue 객체를 사용해야 한다.

## 어떨때 어떻게 쓰냐?

쓰레드는 가볍지만 계산처리 작업에서는 한번에 하나의 스레드에서 작동하기 때문에  
cpu 작업이 적고, I/O 작업이 많은 병렬 처리 프로그램에서 효과를 본다  

프로세스는 각자 고유한 메모리를 가지기 때문에 자원은 더 많이 쓰지만 
병렬로 cpu 작업을 할 수 있고 분산처리 프로그래밍도 가능하다 !!