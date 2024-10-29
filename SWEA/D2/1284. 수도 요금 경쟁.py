# A사 : 1리터당 P원의 돈을 내야 한다.
# B사 : 기본 요금이 Q원이고, 월간 사용량이 R리터 이하인 경우 요금은 기본 요금만 청구된다. 하지만 R 리터보다 많은 양을 사용한 경우 초과량에 대해 1리터당 S원의 요금
# 종민 한 달간 W
T = int(input())

for test_case in range(1, T + 1):
    p, q, r, s, w = map(int, input().split())
    a = w*p
    b = q
    if w>r:
        b+=(w-r)*s
    print(f'#{test_case} {min(a, b)}')