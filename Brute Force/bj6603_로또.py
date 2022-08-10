"""내풀이1 : 조합함수 이용 #이게 제일 빠름
from itertools import combinations
while 1:
    S=list(map(str, input().split()))
    if S[0]=='0': #0이면 break
        break
    print('\n'.join(list(map(' '.join, combinations(S[1:],6))))+'\n')#6개뽑아서 조합만들고 조합 안의 숫자들을 띄어쓰기로 출력, 그 다음 조합은 다음 줄에 출력. 조합 다 구하면 마지막에 줄바꿈.
"""
#내풀이2 : 백트래킹 이용. 당연히 라이브러리 함수 쓰는것보다는 쪼금 느림.
#조합을 구하기 위해 start를 두어 코드 짬.
def dfs(start):
    if len(ans) == 6:
        print(' '.join(map(str, ans)))
        return

    for i in range(start, k):
        if S[i] in ans:
            continue
        ans.append(S[i])
        dfs(i)
        ans.pop()

while 1:
    S=list(map(int, input().split()))
    k=S[0]

    if k==0:
        break

    S=S[1:]
    ans=[]
    dfs(0)
    print()
"""
# 다른 사람 풀이 : 1등
from itertools import combinations
import sys
input=sys.stdin.readline

while 1:
    arr = input().split()

    if arr.pop(0) == '0':
        break

    for i in combinations(arr, 6):
        print(" ".join(i))

    print()
"""

