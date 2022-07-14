import sys
N = int(sys.stdin.readline().rstrip())
d = [i for i in range(N+1)] # i를 제곱수의 합으로 표현 시 제곱수 항의 최대 개수는 i개(1의 제곱 i개가 모이면 i가 되므로)
for i in range(1,N+1):
    for j in range(1,int(i**0.5)+1): # 1<=j*j<=i
        if d[i] > d[i-j*j]+1: #만약 j^2가 마지막으로 더해진 항일 때 j^2+나머지 항의 합이 d[i]보다 작은 경우
            d[i] = d[i-j*j]+1 #나머지 항의 개수 + 1(j*j항)을 d[i]에 저장
print(d[N])
