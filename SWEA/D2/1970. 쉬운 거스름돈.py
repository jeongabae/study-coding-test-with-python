T = int(input())
money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
for test_case in range(1, T + 1):
    n = int(input())
    ans = [0]*8
    for i in range(8):
        ans[i] += n//money[i]
        n %= money[i]
    print(f'#{test_case}')
    print(*ans)