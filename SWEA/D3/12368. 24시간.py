T = int(input())
for test_case in range(1, T + 1):
    a, b = map(int, input().split())
    s = a+b
    if s>23:
        s%=24
    print(f'#{test_case} {s}')