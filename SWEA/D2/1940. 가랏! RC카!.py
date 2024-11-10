T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    dis = 0
    v = 0
    for _ in range(n):
        c = input().split()
        if c[0] == '1':
            v+=int(c[1])
        elif c[0] == '2':
            v-=int(c[1])
            if v<0:
                v=0
        dis+=v

    print(f'#{test_case} {dis}')