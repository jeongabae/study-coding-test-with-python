T = int(input())
for test_case in range(1, T+1):
    s, e, m = map(int, input().split())
    year = 1
    while True:
        if (year-s)%365==0 and (year-e)%24==0 and (year-m)%29==0:
            break
        year+=1
    print(f'#{test_case} {year}')