T = int(input())
for test_case in range(1, T+1):
    arr = list(map(int, input().split()))
    ans = 0
    if arr[0] == arr[1]:
        ans = arr[2]
    elif arr[1] == arr[2]:
        ans = arr[0]
    else:
        ans = arr[1]
    print(f'#{test_case} {ans}')