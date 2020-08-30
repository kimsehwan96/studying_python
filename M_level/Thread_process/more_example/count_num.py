import threading

# counter thread

class CounterThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self, name='Timer Thread')

    # CounterThread가 실행하는 함수
    def run(self):
        global totalCount

        for _ in range(2500000):
            totalCount += 1
        print("2,500,000 카운팅 끝 !!")

if __name__ == '__main__':
    global totalCount
    totalCount = 0

    #total count를 1씩 더하는 스레드 4개 만들어서 돌려보자

    for _ in range(4):
        timerThread = CounterThread()
        timerThread.start()
    
    print("모든 스레드가 종료 될 때 까지 기다린다.")
    mainThread = threading.current_thread()
    for thread in threading.enumerate():
        # Main Thread를 제외한 모든 Thread 들이
        # 카운팅을 완료하고 끝날 때 까지 기다린다
        if thread is not mainThread:
            thread.join()

    print("total count =" + str(totalCount))

'''
모든 스레드가 종료 될 때 까지 기다린다.
2,500,000 카운팅 끝 !!
2,500,000 카운팅 끝 !!
2,500,000 카운팅 끝 !!
2,500,000 카운팅 끝 !!
total count =3826417

같은 변수를 동시에 접근 했기 때문에... 이런 에러가 발생했다고 합니다.

해결 방법 -> 동기화
'''