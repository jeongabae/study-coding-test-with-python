T = int(input())
for test_case in range(1, T + 1):
    arr = list(map(str, input().split()))
    ss = []
    for num in arr:
        s = 0
        for i in num:
            s+=int(i)
        ss.append(s)

    print(f'#{test_case} {max(ss)} {min(ss)}')