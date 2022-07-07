import sys
N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))
ans = [-1] * N # 오큰수가 없는 경우 -1로 남겨 두기 위해
stack = [0] #인덱스 저장 스택

for i in range(1, N):
    while stack and A[stack[-1]] < A[i]:
        ans[stack.pop()] = A[i]

    stack.append(i)

print(*ans)
"""과정 설명
입력 예
4
9 5 4 8
과정
ans [-1, -1, -1, -1] #초기 상태
stack [0] #초기 상태

ans [-1, -1, -1, -1] # A[0] > A[1] 이므로 오큰수 찾지 x. ans[0] = 그대로 -1유지
stack [0, 1] # 스택에 1 추가

ans [-1, -1, -1, -1] # A[1] > A[2] 이므로 오큰수 찾지 x. ans[1] = 그대로 -1유지
stack [0, 1, 2] #  스택에 2 추가

ans [-1, -1, 8, -1] # A[2] < A[3] 이므로 오큰수 찾음. 스택에서 2빼주고 ans[2] = A[3] (8) 해줌
stack [0, 1] #2빼줘서 0,1만 있는 상태

ans [-1, 8, 8, -1] # A[1] < A[3] 이므로 오큰수 찾음. 스택에서 1빼주고 ans[1] = A[3] (8) 해줌
stack [0] #1빼줘서 0만 있는 상태

ans [-1, 8, 8, -1] # A[1] > A[3] 이므로 오큰수 찾지 x.(그래서 ans[0] = 그대로 -1유지, A[3]은 오른쪽에 원소 없으니까 그대로 -1유지)
stack [0, 3] #  스택에 3 추가
출력
-1 8 8 -1
"""
"""이렇게 풀면 시간복잡도가 O(N^2)이라 시간초과 뜰 듯
import sys
N = int(sys.stdin.readline().rstrip())
NGE = list(map(int,sys.stdin.readline().rstrip().split()))
ans = []
for i in range(N):
    if i!=N-1:
        for j in range(i+1,N):
            if NGE[i] < NGE[j]:
                ans.append(NGE[j])
                break
            else:
                if j==N-1:
                    ans.append(-1)

    else:
        ans.append(-1)
print(*ans)
"""
