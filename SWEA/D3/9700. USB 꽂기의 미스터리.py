T = int(input())
for test_case in range(1, T+1):
    p, q = map(float, input().split())
    s1 = (1-p)*q
    s2 = p*(1-q)*q
    ans = "YES" if s1<s2 else "NO"
    print(f'#{test_case} {ans}')