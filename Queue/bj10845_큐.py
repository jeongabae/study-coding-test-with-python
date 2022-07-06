#18258번이랑 코드 같음.
import sys
from collections import deque #큐는 선입선출. 양방향 큐는 데큐.(앞, 뒤 양쪽방향에서 엘리먼트 추가 제거 가능)
def input():
    return sys.stdin.readline().rstrip() #rstrip()을 쓰는게 더 시간 단축!

queue = deque()
N = int(input())
for i in range(N):
    cmd = input().split()
    if cmd[0] == 'push':
        queue.append(cmd[1])
    elif cmd[0] == 'pop':
        print(queue.popleft() if queue else -1)
    elif cmd[0] == 'size':
        print(len(queue))
    elif cmd[0] == 'front':
        print(queue[0] if queue else -1)
    elif cmd[0] == 'back':
        print(queue[-1] if queue else -1)
    elif cmd[0] == 'empty':
        print(1 if not queue else 0)
