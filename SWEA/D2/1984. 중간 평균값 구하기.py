T = int(input())
for test_case in range(1, T + 1):
    arr = sorted(list(map(int, input().split())))
    print(f'#{test_case} {round(sum(arr[1:-1])/8)}')