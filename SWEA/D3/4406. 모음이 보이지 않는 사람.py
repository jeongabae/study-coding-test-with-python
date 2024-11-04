T = int(input())
for test_case in range(1, T + 1):
    a = input()
    ans = ''
    for i in a:
        if i not in ['a', 'e', 'i', 'o', 'u']:
            ans+=i
    print(f'#{test_case} {ans}')