T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    a = [2, 3, 5, 7, 11]
    cnt = [0]*5
    for i in range(5):
        while n%a[i]==0:
            cnt[i] += 1
            n//=a[i]
    print(f'#{test_case}', *cnt)