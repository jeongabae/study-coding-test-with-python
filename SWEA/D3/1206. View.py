import sys
sys.stdin = open("input_1206.txt", "r")
for test_case in range(1, 11):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    for i in range(2, n-2):
        max_h = max(arr[i-2], arr[i-1], arr[i+1], arr[i+2])
        d = arr[i] - max_h
        if arr[i] > max_h:
            ans += d
    print(f'#{test_case} {ans}')