T = int(input())
for test_case in range(1, T+1):
    s = list(input())
    s.reverse()
    dict = {'p':'q', 'q':'p', 'b':'d', 'd':'b'}
    for i in range(len(s)):
        s[i] = dict[s[i]]
    print(f'#{test_case}', ''.join(s))

# 풀이2
# T = int(input())
# for test_case in range(1, T+1):
#     s = input()
#     dict = {'p':'q', 'q':'p', 'b':'d', 'd':'b'}
#     ans = ''
#     for i in s[::-1]:
#         ans+=dict[i]
#     print(f'#{test_case} {ans}')