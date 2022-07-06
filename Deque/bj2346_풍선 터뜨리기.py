#주의 !! 양수가 적혀 있을 경우에는 오른쪽으로, 음수가 적혀 있을 때는 왼쪽으로 이동이라는 말에 헷갈리지 말자!
# 오른쪽으로 이동하려면 왼쪽으로 회전해야하고 왼쪽으로 이동하려면 오른쪽으로 회전해야함!
# 예를 들어 12345 있을 때 1에서 2만큼 오른쪽으로 숫자를 이동시키려면 34512가 되는데
# 이는 2<-3<-4<-5<-1, 3<-4<-5<-1<-2 이렇게 '왼쪽'으로 회전 한 것!! rotate(음수)일 경우 왼쪽으로 회전! 양수인 경우는 오른쪽으로 회전!

import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
queue = deque(enumerate(map(int, input().split())))
ans = []
while queue: #풍선이 다 터져서 없을 때까지
    idx, num = queue.popleft()
    ans.append(idx+1) #인덱스는 0번부터지만 풍선은 1번부터 세기 때문

    if num>0:
        queue.rotate(-(num-1)) #pop해서 왼쪽으로 한칸 이미 이동했기 때문에 num만큼이 아닌 num-1씩 '왼쪽'으로 회전(음수붙여야 함)
    else:
        queue.rotate(-num) # pop해서 왼쪽으로 한칸 이동했지만, num<0인 경우 오른쪽으로 가는 것(회전방향 말함)이므로 상관없이 num번 그대로 회전
                         # 하지만 num이 음수이면 '왼쪽'으로 회전하기 때문에 '오른쪽' 회전하려면 -를 붙여줘야한다!
print(*ans)

"""
입력
5
3 2 1 -3 -1
과정
deque([(0, 3), (1, 2), (2, 1), (3, -3), (4, -1)])
deque([(3, -3), (4, -1), (1, 2), (2, 1)])
deque([(4, -1), (1, 2), (2, 1)])
deque([(2, 1), (1, 2)])
deque([(1, 2)])
deque([])
출력
1 4 5 3 2
"""