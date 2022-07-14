# 11053_가장 긴 증가하는 부분 수열 문제와 비슷한데 발전 문제
import sys
def input():
    return sys.stdin.readline().rstrip()

N = int(input())
A = list(map(int, input().split()))
d = [1]*N #d[i] : A[i]를 마지막으로 하는 가장 긴 증가하는 부분 수열의 길이
prior = [-1]*N # A[i]를 마지막으로 하는 수열에서 A[i] 전 숫자 인덱스 ex) 10-20-10-30이 있으면 30의 prior은 20의 인덱스인 1
for i in range(N):
    for j in range(i):
        if A[i] > A[j] and d[i] < d[j]+1: # 증가하는 수열이여야하므로
                                          # 가장 긴 수열을 구하는 것이므로 d[i] < d[j]+1
                                          # d[j]+1한 값이 지금 d[i]보다 크다면 더 긴 수열을 만들 수 있다는 것이니까 아래처럼 d[i]를 바꿔줌.
            d[i] = d[j]+1
            prior[i] = j

last_num_idx = d.index(max(d))
p = prior[last_num_idx]
ans = [A[last_num_idx]]
while p!=-1:
    ans.append(A[p])
    p = prior[p]
ans.sort()
print(max(d))
print(*ans)

"""내 풀이보다 빠르고 여러 라이브러리 함수 사용한 신박 풀이
from math import inf
import sys
from bisect import bisect_left
input = sys.stdin.readline
input()

l = [-inf]
s = [[]]
for i in map(int, input().split()):
    if l[-1] < i:
        l.append(i)
        s.append(s[-1]+[i])
    else:
        k = bisect_left(l, i)
        l[k] = i
        s[k] = s[k-1]+[i]
print(len(l)-1)
print(*s[-1])
"""