#백준 15661번 스타트와 링크 : 실버2 : 브루트포스, 백트래킹, 조합
# 이거 pypy로 제출해서 맞음 ㅠ
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

def dfs(idx,start,people):  # 지금까지 스타트팀에 i명이 있음.
    global min_diff
    if idx==people:  # 지금까지 뽑은 사람 수가 people명 이라면
        min_diff = min(min_diff, calculate_diff()) #뭐가 더 적은지 선택 후 대입
        return

    for i in range(start, N): #start~N
        if not choice[i]: #start팀이 아니라면
            choice[i] = 1 #start팀으로
            dfs(idx+1,i+1,people) # start팀으로 간 사람이 한 명 늘었으므로 idx+1. start는 지금까지 수열에 있는 수보다 커야하므로 1더해준다.
            choice[i] = 0
for i in range(1,N): #start팀을 i명 뽑는 경우
    dfs(0,0,i)
print(min_diff)
"""다른 사람 풀이
import sys; input = sys.stdin.readline
from itertools import combinations

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
new_S = [sum(i) + sum(j) for i, j in zip(S, zip(*S))]
total_S = sum(new_S) // 2

m = sys.maxsize
for i in range(1, N):
    for c in combinations(new_S[1:], i):
        m = min(m, abs(total_S - sum(c)))
        if not m:
            break
    if not m:
        break
print(m)
"""

"""다른 사람 풀이2
import itertools

INF = float('inf')


def main():
    N = int(input())
    S = [[int(x) for x in input().split()] for _ in range(N)]

    row_sums = [sum(row) for row in S]
    col_sums = [sum(col) for col in zip(*S)]
    stat_by_member = [x + y for x, y in zip(row_sums, col_sums)]
    total = sum(row_sums)
    answer = INF
    for size in range(1, N - 1):
        min_diff = min(
            abs(total - sum(stats))
            for stats in itertools.combinations(stat_by_member, size))
        answer = min(answer, min_diff)

    print(answer)


if __name__ == '__main__':
    main()
    """