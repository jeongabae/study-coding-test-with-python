T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    up = [0]
    down = [0]

    for i in range(n-1):
        diff = arr[i]-arr[i+1]
        if diff<0:
            up.append(diff)
        else:
            down.append(diff)

    print(f'#{test_case} {-min(up)} {max(down)}')