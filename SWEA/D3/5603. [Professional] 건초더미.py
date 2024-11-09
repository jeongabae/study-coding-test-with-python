T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    avg = sum(arr)//n
    ans = 0
    for i in arr:
        if i>avg:
            ans+= i-avg
    print(f'#{test_case} {ans}')