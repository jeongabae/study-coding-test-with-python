# 풀이1
# T = int(input())
# for test_case in range(1, T+1):
#     n, d = map(int, input().split())
#     ans = 0
#     i = 1  # 시작 위치
#
#     while i <= n:
#         ans += 1  # 현재 위치에 물뿌리기 설치
#         i += 2 * d + 1  # 설치된 물뿌리기가 커버하는 다음 위치로 이동
#     print(f'#{test_case} {ans}')
import math
T = int(input())
for test_case in range(1, T+1):
    N, D = map(int, input().split())
    d = D * 2 + 1
    result = math.ceil(N / d)
    print(f'#{test_case} {result}')