def solve(n, m):
    if m==0:
        return 1
    elif m==1:
        return n
    return n*solve(n,m-1)
T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    print(f'#{test_case} {solve(n,m)}')