T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    ans = sum(-i if i%2==0 else i for i in range(1, n+1))
    print(f'#{test_case} {ans}')