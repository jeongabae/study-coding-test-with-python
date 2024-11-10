# T = int(input())
# for test_case in range(1, T + 1):
#     n = int(input())
#     cnt = 0
#     ten = []
#     print(f'#{test_case}')
#     for _ in range(n):
#         c, k = input().split()
#         for i in range(int(k)):
#             cnt+=1
#             if cnt<11:
#                 ten.append(c)
#             else:
#                 cnt=1
#                 print(''.join(ten))
#                 ten = []
#                 ten.append(c)
#     print(''.join(ten))

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    all = ''
    for _ in range(n):
        alpha, num = input().split()
        all += alpha*int(num)
    print(f"#{test_case}")
    for i in range(0, len(all), 10):
        print(all[i:i+10])