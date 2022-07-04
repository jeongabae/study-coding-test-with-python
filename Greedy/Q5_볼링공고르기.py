#import time
n, m = map(int, input().split())
data = list(map(int, input().split()))
#st = time.time()
# 1부터 10까지의 무게를 담을 수 있는 리스트
array = [0] * 11

for x in data:
    # 각 무게에 해당하는 볼링공의 개수 카운트
    array[x] += 1

result = 0
# 1부터 m까지의 각 무게에 대하여 처리
for i in range(1, m + 1):
    n -= array[i] # 무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
    result += array[i] * n # B가 선택하는 경우의 수와 곱해주기

print(result)
#et = time.time()
#print("시간 측정", float(et-st)) #시간 측정 0.0009109973907470703
"""내 풀이
#import time
N, K = map(int, input().split())
w = list(map(int, input().split()))
#st = time.time()
ans = 0
for i in range(N-1): #0~N 인덱스까지
    for j in range(i+1,N): #i번째부터 N 인덱스까지 
        if w[i]!= w[j]:
            ans += 1
print(ans)
#et = time.time()
#print("시간 측정", float(et-st)) #시간 측정 0.0 이 풀이가 더 빠른 듯..??
"""