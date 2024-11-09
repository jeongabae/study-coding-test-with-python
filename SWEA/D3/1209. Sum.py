import sys
sys.stdin = open("input_1209.txt", "r")
# 내 풀이
# for test_case in range(1, 11):
#     t = int(input())
#     arr = [list(map(int, input().split())) for _ in range(100)]
#     arr2 = list(zip(*arr))
#     s = 0
#     for i in arr:
#         s = max(s, sum(i))
#     for i in arr2:
#         s = max(s, sum(i))
#
#     d1 = d2 = 0
#     for i in range(100):
#         d1+=arr[i][i]
#         d2+=arr[i][99-i]
#     s = max(s, d1, d2)
#
#     print(f'#{test_case} {s}')

for test_case in range(1, 11):
    t = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    n = 100
    ans = s3 = s4 = 0
    for i in range(n):
        s1 = s2 = 0
        for j in range(n):
            s1 += arr[i][j]
            s2 += arr[j][i]
        ans = max(ans, s1, s2)

        s3 += arr[i][i]
        s4 += arr[i][n-1-i]
    ans = max(ans, s3, s4)
    print(f'#{test_case} {ans}')