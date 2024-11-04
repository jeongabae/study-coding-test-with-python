T=int(input())
for test_case in range(1,T+1):
    score = list(map(int, input().split()))
    ans = 0
    for i in score:
        if i<40:
            ans+=40
        else:
            ans+=i
    print(f'#{test_case} {ans//5}')