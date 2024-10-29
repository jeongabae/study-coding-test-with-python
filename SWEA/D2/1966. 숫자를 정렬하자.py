T = int(input())
for test_case in range(1, T + 1):
    a = int(input())
    nums = sorted((map(int, input().split())))
    print(f'#{test_case} ', end='')
    print(*nums)