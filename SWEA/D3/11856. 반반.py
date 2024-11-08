T = int(input())
for test_case in range(1, T+1):
    s = list(input())
    s.sort()
    ans = 'Yes' if s.count(s[0])==2 and s.count(s[2])==2 else 'No'
    print(f'#{test_case} {ans}')