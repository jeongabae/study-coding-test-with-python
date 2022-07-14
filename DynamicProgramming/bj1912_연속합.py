import sys
def input():
    return sys.stdin.readline().rstrip()

n = int(input())
d = list(map(int, input().split()))

#  d는 임의의 수열이였는데 이 반복문을 통해 d[i]는 i번째 수로 끝나는 가장 큰 연속합이 된다.
for i in range(1,n):
    # 만약 i번째 수부터 새로운 연속합이 시작되면 d[i] = d[i]
    # 만약 i번째 수가 i-1번째 수의 연속합에 포함되는 경우 d[i-1]+d[i]
    # 두 경우 중 큰 경우 택하여 d[i]에 저장
    d[i] = max(d[i],d[i-1]+d[i])
print(max(d))