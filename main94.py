#data structures(stack)
#from stuck you can just remove the item most recently added
#But make sure using append() and pop() to avoid slow performance
s = []
s.append('small')
s.append('medium')
s.append('large')

#from stuck you can just remove the item most recently added
print(s.pop())
print(s.pop())
print(s.pop())

#LifoQueue
from queue import LifoQueue

st = LifoQueue()
st.put('eat') # <- you shoul consider that LifoQueue' object has no attribute 'append'
st.put('drink')
st.put('pray')

print(st.get())
print(st.get())
print(st.get())


#data structures(queue)
#from queue you remove item least recently added

from collections import deque

q = deque()
q.append('love')
q.append('death')
q.append('robots')

print(q.popleft())
print(q.popleft())
print(q.popleft())


qu = []

qu.append((2, 'walk'))
qu.append((1, 'sleep'))
qu.append((3, 'learn'))

qu.sort(reverse=True)

while qu:
    next_item = qu.pop()
    print(next_item)


