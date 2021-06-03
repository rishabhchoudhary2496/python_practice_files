# The deque is a list optimized for inserting and removing items.

from collections import deque


list_custom = [*'hello this is a big list']
deq = deque(list_custom)
deq.appendleft(' now is the time')
print(deq.count('e')) #return count of item
deq.popleft()
print(deq)