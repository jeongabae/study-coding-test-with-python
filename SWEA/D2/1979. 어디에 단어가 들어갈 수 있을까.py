# T = int(input())
# for test_case in range(1, T + 1):
#     n, k = map(int, input().split())
#     arr = [list(map(int, input().split()))+[0] for _ in range(n)]
#     ans = 0
#     def checkNum(cnt):
#         global ans
#         if cnt == k:
#             ans += 1
#     for i in range(n):
#         cnt1 = cnt2 = 0
#         for j in range(n):
#             if arr[i][j]==0:
#                 checkNum(cnt1)
#                 cnt1=0
#             else:
#                 cnt1+=1
#             if arr[j][i]==0:
#                 checkNum(cnt2)
#                 cnt2=0
#             else:
#                 cnt2+=1
#         checkNum(cnt1)
#         checkNum(cnt2)
#     print(f'#{test_case} {ans}')
def count(arr):
    ret = 0
    for lst in arr:
        cnt = 0
        for j in range(len(lst)):
            if lst[j]:
                cnt += 1
            else:
                if cnt == k:
                    ret += 1
                cnt = 0
    return ret
T = int(input())
for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split()))+[0] for _ in range(n)] + [[0]*(n+1)]
    arr_t = list(map(list, zip(*arr))) # 전치 행렬

    ans = count(arr) + count(arr_t)
    print(f'#{test_case} {ans}')