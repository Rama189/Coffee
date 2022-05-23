#implementing queue using deque

from collections import deque
queue = deque()

queue.append("Mary")
queue.append("John")
queue.append("Susan")

#Now, to remove them from queue in order, use popleft.
queue.popleft()
print(queue)
queue.popleft()
print(queue)