def solve():
    for lst in arr:
        if len(set(lst)) != 9:
            return 0

    for lst in arr2:
        if len(set(lst)) != 9:
            return 0

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            lst = arr[i][j:j+3] + arr[i+1][j:j+3] + arr[i+2][j:j+3]
            if len(set(lst)) != 9:
                return 0
    return 1

T = int(input())
for test_case in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    arr2 = list(zip(*arr))

    ans = solve()
    print(f'#{test_case} {ans}')