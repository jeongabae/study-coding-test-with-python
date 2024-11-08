for test_case in range(1, 11):
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(n):
        max_i = arr.index(max(arr))
        min_i = arr.index(min(arr))
        arr[max_i] -= 1
        arr[min_i] += 1
    print(f'#{test_case} {max(arr)-min(arr)}')
# 풀이2
# for test_case in range(1, 11):
#     n = int(input())
#     arr = list(map(int, input().split()))
#     for i in range(n):
#         arr.sort()
#         arr[0]+=1
#         arr[-1]-=1
#     print(f'#{test_case} {max(arr) - min(arr)}')