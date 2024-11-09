T = int(input())
for test_case in range(1, T+1):
    s = input()
    ans = 'YES' if s.count('o')+15-len(s)>=8 else 'NO'
    print(f'#{test_case} {ans}')