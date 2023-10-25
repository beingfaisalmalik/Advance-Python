from collections import deque
d = deque()
l = [1,2,3,4,5]
rotated_list = []
for i in range(len(l)):
    d.append(l[i])


d.rotate(-1)
for i in range(len(d)):
    rotated_list.append(d[i])
