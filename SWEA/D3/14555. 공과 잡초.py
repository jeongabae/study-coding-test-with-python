T = int(input())
for test_case in range(1, T+1):
    s = input()
    cnt = s.count('(|')+s.count('|)')+s.count('()')
    print(f'#{test_case} {cnt}')