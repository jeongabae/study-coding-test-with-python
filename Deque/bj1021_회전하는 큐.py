import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
s = list(map(int, input().split()))
queue = deque([i for i in range(1,N+1)])
cnt = 0

for i in s:
    idx = queue.index(i)
    if idx==0:
        pass
    elif 0< idx <= len(queue)//2: # 원소가 앞쪽에 있으면 왼쪽으로~~
        queue.rotate(-idx) #왼쪽으로 idx만큼 회전
        cnt += idx
    else: # 원소가 뒤쪽에 있으면 오른쪽으로~~
        queue.rotate(len(queue) - idx) # 오른쪽으로 len(queue) - idx만큼 회전(주의. 이 문제에서는 popleft밖에 못하므로
        # [1,2,3,4,5]에서 4를 뺄때 [5,1,2,3,4]로 만들어서 오른쪽으로 빼는게 아닌 [4,5,1,2,3]으로 만들어서 왼쪽에서 빼야함
        # 그래서 len(queue) - idx - 1이 아닌 len(queue) - idx만큼 회전!
        cnt += len(queue) - idx
    queue.popleft()
print(cnt)

"""내 풀이랑 논리는 똑같은 정석 풀이
import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
arr = list(map(int, input().split()))
queue = deque([i for i in range(1,N+1)])
ans = 0
for i in arr:
    idx = queue.index(i)
    if idx == 0:
        queue.popleft()
    else:
        if idx <= len(queue)//2:
            queue.rotate(-idx)
            queue.popleft()
            ans += idx
        else:
            queue.rotate(len(queue) - idx)
            ans += len(queue) - idx
            queue.popleft()
print(ans)
"""