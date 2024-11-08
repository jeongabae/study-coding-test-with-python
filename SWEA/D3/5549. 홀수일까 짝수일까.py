T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    ans = 'Odd' if n%2!=0 else 'Even'
    print(f'#{test_case} {ans}')