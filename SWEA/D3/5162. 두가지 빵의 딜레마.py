T = int(input())
for test_case in range(1, T+1):
    a, b, c = map(int, input().split())
    ans = 0
    ans += c//min(a,b)
    print(f'#{test_case} {ans}')