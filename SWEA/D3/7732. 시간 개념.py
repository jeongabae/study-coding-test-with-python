T = int(input())
for test_case in range(1, T+1):
    h1, m1, s1 = map(int, input().split(':'))
    h2, m2, s2 = map(int, input().split(':'))
    s1 = h1*3600+m1*60+s1
    s2 = h2*3600+m2*60+s2
    if s1>s2:
        s2+=24*3600
    s = s2-s1
    h = s//3600
    s = s%3600
    m = s//60
    s%=60
    print(f'#{test_case} {h:02d}:{m:02d}:{s:02d}')