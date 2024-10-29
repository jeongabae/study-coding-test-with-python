T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    max_fly = 0
    for si in range(n-m+1):
        for sj in range(n-m+1):
            fly = 0
            for i in range(si, si+m):
                for j in range(sj, sj+m):
                    fly += a[i][j]
            max_fly = max(max_fly, fly)
    print(f'#{test_case} {max_fly}')