import sys
sys.stdin = open("input_1220.txt", "r")
for test_case in range(1, 11):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    arr_t = list(zip(*arr))

    for lst in arr_t:
        prev = 0
        for n in lst:
            if n:
                if n==2 and prev==1:
                    ans += 1
                prev = n

    print(f'#{test_case} {ans}')

# 풀이2
# for test_case in range(1, 11):
#     n = int(input())
#     arr = [list(map(int, input().split())) for _ in range(n)]
#     ans = 0
#
#     for col in range(n):
#         prev = 0
#         for row in range(n):
#             current = arr[row][col]
#             if current:
#                 if current == 2 and prev == 1:
#                     ans += 1
#                 prev = current
#
#     print(f'#{test_case} {ans}')