import sys
def input():
    return sys.stdin.readline().rstrip()

N=int(input())
egg=[list(map(int,input().split())) for _ in range(N)]
ans = 0
def dfs(idx,egg):
    global ans
    if idx == N:
        cnt = 0
        for i in range(N):
            if egg[i][0] <= 0:
                cnt += 1
        if cnt > ans:
            ans = cnt
        return

    if egg[idx][0] <= 0:
        dfs(idx + 1,egg)
    else:
        all_broken = True
        for i in range(N):
            if i != idx and egg[i][0] > 0:
                all_broken = False
                egg[idx][0] -= egg[i][1]
                egg[i][0] -= egg[idx][1]
                dfs(idx + 1, egg)
                egg[idx][0] += egg[i][1]
                egg[i][0] += egg[idx][1]
        if all_broken:
            dfs(idx + 1, egg)
    return

dfs(0,egg)
print(ans)