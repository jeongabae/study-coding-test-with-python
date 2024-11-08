T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]
    ans = 0
    m = n//2
    #방법1
    # for i in range(n):
    #     if i<=m:
    #         for j in range(m-i, m+i+1):
    #             ans += arr[i][j]
    #     else:
    #         for j in range(i-m, n-(i-m)):
    #             ans += arr[i][j]
    #방법2
    s = e = m
    for i in range(n):
        for j in range(s, e+1):
            ans += arr[i][j]
        if i<m:
            s-=1
            e+=1
        else:
            s+=1
            e-=1
    print(f'#{test_case} {ans}')