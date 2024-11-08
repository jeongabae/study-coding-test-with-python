T = int(input())
for test_case in range(1, T+1):
    a = list(input().split())
    ans = []
    for i in a:
        ans.append(i[0].upper())
    print(f'#{test_case}', ''.join(ans))