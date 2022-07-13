# 실버 1
# 11052 카드 구매하기와 비슷
import sys
def input():
    return sys.stdin.readline().rstrip()

N = int(input())
P = [0]+list(map(int,input().split())) # 0개 구매 시 0원이므로 0 추가해줌.
d = P # d[i] = 카드 i개를 갖기 위해 지불해야 하는 금액의 최소값
               # P를 붙이는 이유 : 만약 4개를 구매하고싶다고하면
               # 4장들어있는 카드 팩(P4)을 사기 위한 값이, 다른 팩들을 조합해서 샀을 떄의 금액 보다 높을 수 있기 때문에 일단 먼저 저장해놓음.

for i in range(1,N+1):
    for j in range(1,i+1):
        d[i] = min(d[i],P[j]+d[i-j])
print(d[N])