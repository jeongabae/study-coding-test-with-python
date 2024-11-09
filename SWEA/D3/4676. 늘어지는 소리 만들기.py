T = int(input())
for test_case in range(1, T+1):
    s = list(input())
    h = int(input())
    hp = list(map(int, input().split()))
    hp.sort()

    for i in range(h):
        s.insert(hp[i]+i, '-')
    print(f'#{test_case}', ''.join(s))