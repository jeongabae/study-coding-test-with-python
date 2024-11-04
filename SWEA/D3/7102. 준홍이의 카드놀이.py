T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    s = []
    cnt = [0]*(n+m+1)

    for i in range(1, n+1):
        for j in range(1, m+1):
            s.append(i+j)

    for i in s:
        cnt[i]+=1

    max_cnt = max(cnt)
    num = [i for i, count in enumerate(cnt) if count == max_cnt]
    print(f'#{test_case}', *num)