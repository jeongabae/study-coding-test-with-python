T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    ans = 'No'
    for i in range(1,10):
        for j in range(1,10):
            if i*j==n:
                ans = 'Yes'
                break
    print(f'#{test_case} {ans}')