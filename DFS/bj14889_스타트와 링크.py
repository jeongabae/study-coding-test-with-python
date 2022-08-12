#백준 14889번 스타트와 링크 : 실버2 : 브루트포스, 백트래킹, 조합
#내풀이1 : 조합이용 풀이. 이게 시간은 더 빠르지만 메모리는 더 큼
from itertools import combinations
import sys
def input():
    return sys.stdin.readline().rstrip()

N = int(input()) #축구를 하기 위해 모인 사람은 총 N명
S = [list(map(int, input().split())) for _ in range(N)] #능력치 행렬
choice = [0]*N #팀 결정 1이면 start팀 0이면 link팀.
min_diff = sys.maxsize #int의 최대값이 sys.maxsize이므로 이렇게 일단 해둠.

def calculate_diff():
    team_start=0 #start팀의 능력치 합
    team_link=0 #link팀의 능력치 합
    for i in range(N-1):
        for j in range(i+1,N):
            if choice[i] and choice[j]: #만약 i,j번이 1(start팀)이라면
                team_start += S[i][j] + S[j][i]
            elif not choice[i] and not choice[j]:  #만약 i,j번이 0(link팀)이라면
                team_link += S[i][j] + S[j][i]
    return abs(team_start-team_link)

for i in list(combinations(range(0,N), N//2)): #N에서 절반 만큼 start팀을 할 사람을 뽑아서
    choice = [0] * N
    for j in range(len(i)):
        choice[i[j]] = 1 #start팀이라고 표시해준다.

    min_diff = min(min_diff, calculate_diff()) #뽑았으니 뭐가 더 작은지 비교 후 대입

print(min_diff)
"""# 내풀이2 : 백트래킹 이용. 이 풀이는 풀이1인 조합 이용 풀이보다 시간은 더 느리지만 메모리 더 적게 씀
import sys
def input():
    return sys.stdin.readline().rstrip()

N = int(input()) #축구를 하기 위해 모인 사람은 총 N명
S = [list(map(int, input().split())) for _ in range(N)] #능력치 행렬
choice = [0]*N #팀 결정 1이면 start팀 0이면 link팀. 
min_diff = sys.maxsize #int의 최대값이 sys.maxsize이므로 이렇게 일단 해둠.

def calculate_diff():
    team_start=0 #start팀의 능력치 합
    team_link=0 #link팀의 능력치 합
    for i in range(N-1):
        for j in range(i+1,N):
            if choice[i] and choice[j]: #만약 i,j번이 1(start팀)이라면
                team_start += S[i][j] + S[j][i]
            elif not choice[i] and not choice[j]:  #만약 i,j번이 0(link팀)이라면
                team_link += S[i][j] + S[j][i]
    return abs(team_start-team_link)

def dfs(start):
    global min_diff
    if choice.count(1) == N // 2:  # start팀에 N의 절반만큼 사람이 왔다면!
        min_diff = min(min_diff, calculate_diff()) #뭐가 더 적은지 선택 후 대입
        return

    for i in range(start, N): #start~N
        if not choice[i]: #start팀이 아니라면
            choice[i] = 1 #start팀으로
            dfs(i+1) #start는 지금까지 수열에 있는 수보다 커야하므로 1더해준다.
            choice[i] = 0


dfs(0)
print(min_diff)
"""