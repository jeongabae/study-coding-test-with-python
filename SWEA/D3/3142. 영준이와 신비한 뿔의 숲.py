# 풀이1
# T = int(input())
# for test_case in range(1, T+1):
#     n, m = map(int, input().split())
#     for i in range(m+1):
#         for j in range(m+1):
#             if i+2*j==n and i+j==m:
#                 x, y = i, j
#                 break
#     print(f'#{test_case} {x} {y}')

T = int(input())
for test_case in range(1, T+1):
    n, m = map(int, input().split())
    y = n-m
    x = m-y
    print(f'#{test_case} {x} {y}')