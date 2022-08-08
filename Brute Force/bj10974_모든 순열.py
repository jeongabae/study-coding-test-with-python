import sys

def next_permutations(li): #다음 순열 구하는 함수
    # 1. a[i-1] < a[i]를 만족하는 가장 큰 i를 찾는다.
    i = n - 1
    while (a[i - 1] >= a[i] and i > 0):  # a[i-1] < a[i]를 만족하지 않는 경우 즉,a[i-1]>=a[i] 그리고 i<0이면 그 전 인덱스 확인.
        i -= 1

    # i<=0이 되면 다 내림차순이란 소리..!(즉 맨 마지막 순열)
    if i <= 0:
        return -1

    # 2. i<=j이면서 a[i-1]<a[j]를 만족하는 가장 큰 j를 찾는다.
    else:
        j = n - 1
        while (a[i - 1] >= a[j]):
            j -= 1

        # 3. a[i-1]과 a[j]를 swap한다.(바꿔준다.)
        a[i - 1], a[j] = a[j], a[i - 1]

        # 4. i번째의 값부터 그 이후 값 모두를 오름차순 정렬
        sort_from_jth_of_a = a[i:]
        sort_from_jth_of_a.sort()
        ans = a[:i] + sort_from_jth_of_a

        # 출력
        print(*ans)
        return ans

n=int(sys.stdin.readline().rstrip())
a=[i for i in range(1,n+1)]
print(*a)
while 1:
    a = next_permutations(a)

    if a==-1:
        break
"""1등 풀이 : itertools의 permutations함수 이용한게 젤 빠름
from itertools import permutations
import sys
print=sys.stdout.write
def BOJ10974():
    n = int(input())
    for i in map(" ".join,permutations([str(i) for i in range(1,n+1)])):
        print(i+"\n")
BOJ10974()
"""
"""이것도 똑같이 permutations함수 이용 풀이
from itertools import permutations #순열 함수

N = int(input())
N_list = [i for i in range(1, N+1)]

for numbers in list(permutations(N_list)):
    for num in numbers:
        print(num, end=' ')
    print()
"""
"""다른 사람 풀이 : dfs를 이용한 백트래킹
n = int(input())
temp = []

def dfs():
    if len(temp) == n:
        print(*temp)
        return
    for i in range(1, n + 1):
        if i not in temp:
            temp.append(i)
            dfs()
            temp.pop()

dfs()
"""