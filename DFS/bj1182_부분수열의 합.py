import sys
def input():
    return map(int, sys.stdin.readline().split())
N, S = input()
a = list(input())
used = [0] * (N)
ans = []
cnt = 0

def dfs(idx,start):
    global cnt
    if idx>N:
        return
    if len(ans) and sum(ans)==S:
        cnt +=1

    for i in range(start, N):
        if not used[i]:
            used[i] = 1
            ans.append(a[i])
            dfs(idx + 1,i+1)
            used[i] = 0
            ans.pop()
dfs(0,0)
print(cnt)
"""다른 사람 풀이 : 내꺼보다 2배정도 빠름
import sys
input = sys.stdin.readline
def dfs(idx, sum):
    global cnt
    if idx >= n:
        return
    sum += s_[idx]
    if sum == s:
        cnt += 1
    dfs(idx + 1, sum - s_[idx])
    dfs(idx + 1, sum)
n, s = map(int, input().split())
s_ = list(map(int, input().split()))
cnt = 0
dfs(0, 0)
print(cnt)
"""
""" 다른 사람 풀이 : 조합 함수 이용 (제일 빠름)
import sys
from itertools import combinations

input = sys.stdin.readline
n, s = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
for i in range(1, n+1):
    comb = combinations(arr, i)

    for x in comb:
        if sum(x) == s:
            cnt += 1

print(cnt)
"""