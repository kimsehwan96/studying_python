import queue

data_queue = queue.Queue()

data_queue.put("hello")
data_queue.put(1)

print(data_queue.qsize())

data_queue.get() # >>> hello

data_queue.qsize() # >>> 1
data_queue.get() # >>> 1
data_queue.qsize() # >>> 0
