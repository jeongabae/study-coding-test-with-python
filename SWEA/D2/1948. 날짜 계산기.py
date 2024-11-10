T = int(input())
days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for test_case in range(1, T + 1):
    m1, d1, m2, d2 = map(int, input().split())
    sum1 = sum(days[:m1]) + d1
    sum2 = sum(days[:m2]) + d2
    ans = sum2-sum1 + 1
    print(f'#{test_case} {ans}')