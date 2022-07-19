import sys
def input():
    return sys.stdin.readline().rstrip()

N = int(input())
A = list(map(int, input().split()))
d = A.copy() #d[i] : A[i]를 마지막으로 하는 가장 긴 증가하는 부분 수열의 합
for i in range(N):
    for j in range(i):
        if A[i] > A[j] and d[i] < d[j]+A[i]: # 증가하는 수열이여야하므로
                                          #  합이 가장 큰 증가 부분 수열을 구하는 것이므로 d[i] < d[j]+A[i]
                                          # d[j]+A[i]한 값이 지금 d[i]보다 크다면 더 합이 큰 수열을 만들 수 있다는 것이니까 아래처럼 d[i]를 바꿔줌.
            d[i] = d[j]+A[i]
print(max(d))