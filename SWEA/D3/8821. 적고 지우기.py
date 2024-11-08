T = int(input())
for test_case in range(1, T+1):
    s = input()
    ans = []
    for i in s:
        if i in ans:
            ans.remove(i)
        else:
            ans.append(i)
    print(f'#{test_case} {len(ans)}')