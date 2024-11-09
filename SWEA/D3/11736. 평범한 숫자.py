T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(1, n-1):
        min_p = min(p[i-1:i+2])
        max_p = max(p[i-1:i+2])
        if p[i]!=min_p and p[i]!=max_p:
            ans+=1
    print(f'#{test_case} {ans}')