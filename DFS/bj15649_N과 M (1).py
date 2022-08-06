import sys
N, M = map(int, sys.stdin.readline().split())
used = [0] * (N + 1)
ans = []

def dfs(idx): #idx는 몇 번째에 있느냐를 의미 만약에 1 2 3이라는 수열이면 1은 idx=0자리 2는 idx=1, 3는 idx=3
    if idx==M:#만약 길이가 M=3인 수열을 만드는데 idx가 3이면 0,1,2 세 개의 숫자가 찼다는거니까 수열 출력
        print(' '.join(ans))
        return

    for i in range(1, N+1):#길이가 M이 아니라면 1부터 N까지의 숫자를 확인
        if not used[i]: #중복 없어야 하므로.. 만약에 수열에 숫자i가 아직 없다면
            used[i] = 1 #방문(사용) 처리를해주고,
            ans.append(str(i)) #그 숫자를 수열에 넣는다.
            dfs(idx + 1) #그리고 그 다음 수가 뭐가 올 수 있을지 찾는다.(가지치기)
            used[i] = 0 #어떤 수열을 찾았으므로 다음 수열을 찾기 위해 수 하나를 꺼내준다. 즉, 방문(사용)하지 않았다고 표시.
            ans.pop() # 수열에서 수를 꺼냄
dfs(0) #0번째 수부터 길이가 M인 수열을 만들자.
"""테스트
import sys
N, M = map(int, sys.stdin.readline().split())
visited = [0]*(N+1)
ans = []

def dfs(cnt):
    if cnt==M:
        print(' '.join(ans))
        return

    for i in range(1, N+1):
        print("1. i",i,"cnt",cnt,"vis",visited)
        print("ans",ans)
        if not visited[i]:
            visited[i] = 1
            ans.append(str(i))
            print("2. i", i, "cnt",cnt,"vis", visited)
            print("ans", ans)
            dfs(cnt+1)
            visited[i] = 0
            ans.pop()
            print("3. i", i,"cnt",cnt, "vis", visited)
            print("ans", ans)
dfs(0)
"""
"""str말고 숫자를 리스트에 저장해서 unzip하는 경우 좀 더 느렸다..
import sys
N, M = map(int, sys.stdin.readline().split())
visited = [0]*(N+1)
ans = []

def dfs(cnt):
    if cnt==M:
        print(*ans)
        return

    for i in range(1, N+1):
        if not visited[i]:
            visited[i] = 1
            ans.append(i)
            dfs(cnt+1)
            visited[i] = 0
            ans.pop()
dfs(0)
"""
"""다른 사람 풀이
n, m = map(int, input().split())

s = []
def f():
  if len(s) == m:
    print(' '.join(map(str, s)))
    return

  for i in range(1, n + 1):
    if i in s:
      continue
    s.append(i)
    f()
    s.pop()

f()
"""

"""다른 사람 풀이 : itertools 라이브러리의 permutations 함수 이용해서 푼 풀이 permutations(list, M) list에서 M개 뽑기
from itertools import permutations

N, M = map(int, input().split())
case = permutations(range(1,N+1), M)

for i in case:
    for j in i:
        print(j, end=" ")
    print()
    """
"""순열 함수 이용 풀이2 (1등 풀이)
from itertools import permutations

N, M = map(int, input().split())
li = map(str, range(1, N+1))
print('\n'.join(list(map(' '.join,permutations(li, M)))))
"""

"""다른 사람 풀이
N, M = map(int, input().split())


def solve(cnt, s):
    if cnt == M:  # M개를 골랐으면 종료
        print(" ".join(s))
        return

    for num in [str(i) for i in range(1, N + 1)]:
        if num not in s:  # 이미 고르지 않은 숫자를 고르게 함
            solve(cnt + 1, s + [num])


solve(0, [])
"""

"""
# Authored by : tony9402
# Co-authored by : -
# Link : http://boj.kr/69f68131effd4506a17fdac4b8569c6c
import sys

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
choose = [ 0 for _ in range(10) ]
used   = [ 0 for _ in range(10) ]

def dfs(cnt):
    global N, M
    if cnt == M:
        for idx in range(cnt):
            print(choose[idx], end=' ')
        print()
        return

    for i in range(1, N + 1):
        if used[i]:
            continue
        used[i] = 1
        choose[cnt] = i
        dfs(cnt + 1)
        used[i] = 0

dfs(0)
"""