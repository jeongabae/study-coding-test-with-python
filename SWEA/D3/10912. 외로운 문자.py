T = int(input())
for test_case in range(1, T+1):
    s = list(input())
    ans = ''
    s.sort()
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            s[i] = s[i+1] = ''
    ans = ''.join(s)
    ans = ans if ans else 'Good'
    print(f'#{test_case} {ans}')