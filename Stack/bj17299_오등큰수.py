import sys
from collections import Counter
N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))
A_cnt = Counter(A)

ans = [-1] * N # 오등큰수가 없는 경우 -1로 남겨 두기 위해
stack = [0] #인덱스 저장 스택 #처음 검사해야할 인덱스는 0이므로 0저장
print("A_cnt",A_cnt)
print("ans",ans)
print("stack",stack)
for i in range(1, N):
    while stack and A_cnt[A[stack[-1]]] < A_cnt[A[i]]:
        ans[stack.pop()] = A[i]
        print("ans", ans)
        print("stack", stack)
    stack.append(i)
    print("ans", ans)
    print("stack",stack)


print(*ans)
"""과정 설명
입력
7
1 1 2 3 4 2 1

설명
A_cnt : Counter({1: 3, 2: 2, 3: 1, 4: 1})
ans [-1, -1, -1, -1, -1, -1, -1] #초기 상태
stack [0] #초기 상태
ans [-1, -1, -1, -1, -1, -1, -1] #i=1 #A_cnt[1] (3) = A_cnt(1) 이므로 오등큰수 못 찾음
stack [0, 1] #스택에 1 추가
ans [-1, -1, -1, -1, -1, -1, -1] #i=2  #A_cnt[1] (3) > A_cnt(2) (2) 이므로 오등큰수 못 찾음
stack [0, 1, 2] #스택에 2 추가
ans [-1, -1, -1, -1, -1, -1, -1] #i=3 #A_cnt[2] (2) > A_cnt(3) (1) 이므로 오등큰수 못 찾음
stack [0, 1, 2, 3] #스택에 3 추가
ans [-1, -1, -1, -1, -1, -1, -1] #i=4 #A_cnt[3] (1) > A_cnt(4) (1) 이므로 오등큰수 못 찾음
stack [0, 1, 2, 3, 4] #스택에 4 추가
ans [-1, -1, -1, -1, 2, -1, -1] #i=5  #A_cnt[4] (1) < A_cnt(2) (2) 이므로 오등큰수 찾음. 스택에서 4빼고 ans[4] = A[5] (2) 저장
stack [0, 1, 2, 3] #스택에서 4뺀 모습
비슷하게 아래도 해주면 됨.
ans [-1, -1, -1, 2, 2, -1, -1]
stack [0, 1, 2]
ans [-1, -1, -1, 2, 2, -1, -1]
stack [0, 1, 2, 5]
ans [-1, -1, -1, 2, 2, 1, -1]
stack [0, 1, 2]
ans [-1, -1, 1, 2, 2, 1, -1]
stack [0, 1]
ans [-1, -1, 1, 2, 2, 1, -1]
stack [0, 1, 6]
-1 -1 1 2 2 1 -1
"""
"""시간초과 난 풀이
import sys
N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))
A_cnt =[A.count(i) for i in A] 
ans = [-1] * N # 오등큰수가 없는 경우 -1로 남겨 두기 위해
stack = [0] #인덱스 저장 스택

for i in range(1, N):
    while stack and A_cnt[stack[-1]] < A_cnt[i]:
        ans[stack.pop()] = A[i]
    stack.append(i)

print(*ans)
"""