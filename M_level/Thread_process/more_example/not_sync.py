import threading

tot = 0

def add_total(amount):
    global tot
    tot += amount
    print(threading.current_thread().getName() + "Not sync : ", tot)


if __name__ == "__main__":
    for i in range(10000):
        my_thread = threading.Thread(
            target = add_total, args = (1,)
        )
    
        my_thread.start()