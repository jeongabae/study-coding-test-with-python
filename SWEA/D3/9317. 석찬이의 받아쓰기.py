T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    a = input()
    b = input()
    cnt = 0

    for i in range(n):
        if a[i]==b[i]:
            cnt+=1

    print(f'#{test_case} {cnt}')