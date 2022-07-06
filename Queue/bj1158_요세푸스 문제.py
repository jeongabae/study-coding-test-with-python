import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

N, K = map(int, input().split())
queue = deque([i for i in range(1,N+1)])
s = []

for j in range(N):
    queue.rotate(-(K-1))
    s.append(queue.popleft())
print("<", ', '.join(str(i) for i in s), ">", sep="")

"""1등분 코드 : 이 분은 deque안쓰고 list로만 쓰심.
n, m = map(int, input().split())
l = list(range(1, n + 1))
r = []
index = 0

while l:
    index = (index + m - 1) % len(l)
    r.append(str(l.pop(index)))

print('<', ', '.join(r), '>', sep='')
"""