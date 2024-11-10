T = int(input())
for test_case in range(1, T + 1):
    h1, m1, h2, m2 = map(int, input().split())
    h = h1+h2
    res_h = h if h<13 else h%12
    m = m1+m2
    res_m = m if m<61 else m%60
    res_h += m//60
    print(f'#{test_case} {res_h} {res_m}')