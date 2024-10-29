T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if n > m:
        a, b = b, a
        n, m = m, n

    s_max = 0
    for i in range(m - n + 1):
        s = sum(a[j] * b[j + i] for j in range(n))
        s_max = max(s_max, s)

    print(f'#{test_case} {s_max}')