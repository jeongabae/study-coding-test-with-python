T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    ans = n+ arr[0]+arr[-1]
    for i in range(n-1):
        ans += max(arr[i], arr[i+1])
    print(f'#{test_case} {ans}')