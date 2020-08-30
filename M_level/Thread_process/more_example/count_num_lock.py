import threading


#공유된 변수를 위한 클래스

class ThreadVar():
    def __init__(self):
        self.lock = threading.Lock()
        self.lockedValue = 0

    def plus(self, value):
        self.lock.acquire()
        try:
            self.lockedValue += value
        finally:
            self.lock.release()
            # 최종적으로 LOCK을 해결해서 다른 스레드에서 사용 가능하게 해줘야 한다.
# counter thread

class CounterThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self, name='Timer Thread')

    # CounterThread가 실행하는 함수
    def run(self):
        global totalCount

        for _ in range(2500000):
            totalCount.plus(1)
        print("2,500,000 카운팅 끝 !!")

if __name__ == '__main__':
    global totalCount
    totalCount = ThreadVar()

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

    print("total count =" + str(totalCount.lockedValue))
