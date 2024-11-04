T = int(input())
for test_case in range(1, T + 1):
    origin = list(input())
    l = len(origin)
    initial = ['0']*l
    cnt = 0

    for i in range(l):
        if initial==origin:
            break
        if initial[i]!=origin[i]:
            initial[i:] = origin[i]*len(initial[i:])
            cnt+=1

    print(f'#{test_case} {cnt}')