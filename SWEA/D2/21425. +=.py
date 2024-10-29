T = int(input())
for test_case in range(1, T + 1):
    a, b, n = map(int, input().split())
    cnt = 0
    while a <= n and b <= n:
        if a < b:
            a += b
        else:
            b += a
        cnt += 1
    print(cnt)