T = int(input())
for test_case in range(1, T + 1):
    a, b = map(int, input().split())
    ans = -1
    if a<10 and b<10:
        ans = a*b
    print(f'#{test_case} {ans}')