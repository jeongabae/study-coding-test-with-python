T = int(input())
for test_case in range(1, T+1):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    print(f'#{test_case} {sum(arr[:k])}')