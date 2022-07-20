import sys
def input():
    return sys.stdin.readline().rstrip()

n = int(input())
s = list(map(int, input().split()))
d = s.copy()
d_remove = [-1000]*n

#  d는 임의의 수열이었는데 이 반복문을 통해 d[i]는 i번째 수로 끝나는 가장 큰 연속합이 됨.
for i in range(1,n):
    # 경우 1)
    # 만약 i번째 수부터 새로운 연속합이 시작되면 d[i] = s[i]
    # 만약 i번째 수가 i-1번째 수의 연속합에 포함되는 경우 d[i-1]+s[i]
    # 두 경우 중 큰 경우 택하여 d[i]에 저장
    d[i] = max(s[i],d[i-1]+s[i]) #이 줄에서는 s[i]대신 d[i]써도 됨.
    d_remove[i] = max(d[i-1],d_remove[i-1]+s[i]) # 경우2) i번째 원소를 제거하는 경우 i번째 원소를 제거하였기 때문에 s[i]를 더하지 X ->d[i-1]
                                                 # i번째 전에 이미 원소를 제거한 적 있어, i번째 원소를 선택하는 경우 -> d_remove[i-1]+s[i]
print(max(d+d_remove))