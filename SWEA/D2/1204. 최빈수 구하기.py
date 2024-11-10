T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    cnt = [0]*(max(arr)+1)
    for i in arr:
        cnt[i] += 1
    max_count = max(cnt)
    ans = max([i for i, count in enumerate(cnt) if count == max_count])
    print(f'#{test_case} {ans}')