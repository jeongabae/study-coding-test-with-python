T = int(input())
for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    print(f'#{test_case}', end=' ')
    print(1 if n%k else 0)