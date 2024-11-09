from itertools import combinations
T = int(input())
for test_case in range(1, T+1):
    arr = list(map(int, input().split()))
    c = list(combinations(arr, 3))
    ans = []
    for row in c:
        s = sum(row)
        if s not in ans:
            ans.append(s)
    ans.sort(reverse=True)
    print(f'#{test_case} {ans[4]}')