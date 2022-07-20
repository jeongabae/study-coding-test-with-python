import sys
def input():
    return sys.stdin.readline().rstrip()

N = int(input())
A = list(map(int, input().split()))
A_rev = list(reversed(A))

d = [1]*N #d[i] : A[i]를 마지막으로 하는 가장 긴 증가하는 부분 수열의 길이
d2 = [1]*N #A를 거꾸로 해서 즉, 뒤에서부터 가장 긴 증가하는 부분 수열의 길이를 구한다.

for i in range(N):
    for j in range(i):
        if A[i] > A[j] and d[i] < d[j]+1: #A[i]를 마지막으로 하는 가장 긴 증가하는 부분 수열의 길이 구하기.
            d[i] = d[j]+1
        if A_rev[i] > A_rev[j] and d2[i] < d2[j] + 1: #뒤에서부터 가장 긴 증가하는 부분 수열의 길이를 구한다.
            d2[i] = d2[j] + 1
d2.reverse() # 거꾸로 뒤집어서 구했으므로 다시 돌려준다.
print(max((d[i]+d2[i]-1 for i in range(N))))

"""나보다 빠른 신박 풀이 : 이진 탐색 라이브러리인 bisect 이용
import bisect as b
input()
def g(s):
    l,v=[],[]
    for i in s:
        j=b.bisect_left(l,i)
        if j==len(l):l+=[i]
        else:l[j]=i
        v+=[j+1]
    return v
s=[*map(int,input().split())][::-1]
print(max(x+y-1 for x,y in zip(g(s),g(s[::-1])[::-1])))
"""