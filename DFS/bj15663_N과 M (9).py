# 풀이 1 : 중복되는 수열을 여러 번 출력하면 안되므로 변수 하나를 둬서 중복 방지.

import sys
def input():
    return map(int, sys.stdin.readline().split())
N, M = input()
a = list(input())
a.sort() #수열은 사전 순으로 증가하는 순서로 출력해야 하므로..정렬..!
used = [0] * (N + 1)
ans = []

def dfs(idx): #idx는 몇 번째에 있느냐를 의미 만약에 1 2 3이라는 수열이면 1은 idx=0자리 2는 idx=1, 3는 idx=3
    if idx==M:#만약 길이가 M=3인 수열을 만드는데 idx가 3이면 0,1,2 세 개의 숫자가 찼다는거니까 수열 출력
        print(' '.join(ans)) #출력한 적 없으면 출력
        return
    before_num = 0
    for i in range(1, N+1):#길이가 M이 아니라면 1부터 N까지의 숫자를 확인
        print("1 ans",ans)
        print("1 before",before_num, "a[i-1]",a[i-1])
        if not used[i] and before_num != a[i-1]: #중복 없어야 하므로.. 만약에 수열에 숫자 a[i-1]가 아직 없다면
            used[i] = 1 #방문(사용) 처리를해주고,
            ans.append(str(a[i-1])) #그 숫자를 수열에 넣는다.
            before_num = a[i-1]
            print("2 ans", ans)

            print("2 before", before_num, "a[i-1]", a[i - 1])
            dfs(idx + 1) #그리고 그 다음 수가 뭐가 올 수 있을지 찾는다.(가지치기)
            used[i] = 0 #어떤 수열을 찾았으므로 다음 수열을 찾기 위해 수 하나를 꺼내준다. 즉, 방문(사용)하지 않았다고 표시.
            ans.pop() # 수열에서 수를 꺼냄
            print("3 ans", ans)

            print("3 before", before_num, "a[i-1]", a[i - 1])
dfs(0) #0번째 수부터 길이가 M인 수열을 만들자.

# 풀이2 : all_ans를 리스트가 아닌 dict 자료형(해쉬)으로 밤꿨더니 성공!
# 그 이유는 list는 검색 시간 복잡도가 O(N)인데 dict는 검색 시간 복잡도가 O(1)..!! 빠른...~~
import sys
def input():
    return map(int, sys.stdin.readline().split())
N, M = input()
a = list(input())
a.sort()
used = [0] * (N + 1)
ans = []
all_ans = {}

def dfs(idx):
    if idx==M:
        num = ' '.join(ans)
        if num not in all_ans: #시간복잡도...리스트에서의 검색 보다 빠른 O(N)
            print(num)
            all_ans[num] = 1
        return

    for i in range(1, N+1):
        if not used[i]:
            used[i] = 1
            ans.append(str(a[i-1]))
            dfs(idx + 1)
            used[i] = 0
            ans.pop()
dfs(0)
"""시간 초과난 코드
import sys
def input():
    return map(int, sys.stdin.readline().split())
N, M = input()
a = list(input())
a.sort() #수열은 사전 순으로 증가하는 순서로 출력해야 하므로..정렬..!
used = [0] * (N + 1)
ans = []
all_ans = []

def dfs(idx): #idx는 몇 번째에 있느냐를 의미 만약에 1 2 3이라는 수열이면 1은 idx=0자리 2는 idx=1, 3는 idx=3
    if idx==M:#만약 길이가 M=3인 수열을 만드는데 idx가 3이면 0,1,2 세 개의 숫자가 찼다는거니까 수열 출력
        if ' '.join(ans) not in all_ans: # 중복되는 수열을 여러 번 출력하면 안되므로 이미 출력한적 있는 답인지 확인 #시간복잡도 O(n)
            print(' '.join(ans)) #출력한 적 없으면 출력
            all_ans.append(' '.join(ans)) #그리고 답안에 더해줌
        return

    for i in range(1, N+1):#길이가 M이 아니라면 1부터 N까지의 숫자를 확인
        if not used[i]: #중복 없어야 하므로.. 만약에 수열에 숫자 a[i]가 아직 없다면
            used[i] = 1 #방문(사용) 처리를해주고,
            ans.append(str(a[i-1])) #그 숫자를 수열에 넣는다.
            dfs(idx + 1) #그리고 그 다음 수가 뭐가 올 수 있을지 찾는다.(가지치기)
            used[i] = 0 #어떤 수열을 찾았으므로 다음 수열을 찾기 위해 수 하나를 꺼내준다. 즉, 방문(사용)하지 않았다고 표시.
            ans.pop() # 수열에서 수를 꺼냄
dfs(0) #0번째 수부터 길이가 M인 수열을 만들자.
"""

"""다른 사람 풀이 : 풀이 1과 사실상 같은 풀이
# Authored by : tony9402
# Co-authored by : -
# Link : http://boj.kr/186f2997e3dd48859f2ef8b729d98bf3
import sys

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
arr  = sorted(list(map(int, input().split())))
choose = [ 0 for _ in range(10) ]
used   = [ 0 for _ in range(10) ]

def dfs(cnt):
    global N, M
    if cnt == M:
        for idx in range(cnt):
            print(arr[choose[idx]], end=' ')
        print()
        return

    pre = -1
    for i in range(N):
        if used[i] or pre == arr[i]:
            continue
        pre = arr[i]
        used[i] = 1
        choose[cnt] = i
        dfs(cnt + 1)
        used[i] = 0

dfs(0)
"""