T = int(input())
for test_case in range(1, T + 1):
    l, u, x = map(int, input().split())
    ans = 0
    if x>u:
        ans = -1
    elif x<l:
        ans = l-x
    print(f'#{test_case} {ans}')
