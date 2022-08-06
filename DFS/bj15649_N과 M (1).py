import sys
N, M = map(int, sys.stdin.readline().split())
visited = [0]*(N+1)
ans = []

def dfs(cnt):
    if cnt==M:
        print(' '.join(ans))
        return

    for i in range(1, N+1):
        if not visited[i]:
            visited[i] = 1
            ans.append(str(i))
            dfs(cnt+1)
            visited[i] = 0
            ans.pop()
dfs(0)
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
"""순열 함수 이용 풀이2
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