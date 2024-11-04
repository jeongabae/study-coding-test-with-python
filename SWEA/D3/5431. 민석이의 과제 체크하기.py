# T = int(input())
# for test_case in range(1, T + 1):
#     n, k = map(int, input().split())
#     arr = list(map(int, input().split()))
#     st = [0]*(n+1)
#
#     for i in range(k):
#         st[arr[i]] = 1
#
#     print(f'#{test_case}', end=' ')
#     for i in range(1, n+1):
#         if not st[i]:
#             print(i, end=' ')
#     print()
T = int(input())
for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = []
    for i in range(1, n+1):
        if i not in arr:
            ans.append(i)

    print(f'#{test_case}', *ans)