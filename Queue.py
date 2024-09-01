from collections import deque

queue = deque()

def queue_append(value):
    queue.append(value)
    print('append: ', queue)

def queue_pop():
    queue.popleft()
    print('pop: ', queue)

queue_append(5)
queue_append(7)
queue_pop()
queue_append(1)
queue_append(3)
queue_pop()
queue_pop()
