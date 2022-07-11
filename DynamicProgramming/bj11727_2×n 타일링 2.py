# 11726번과 비슷
import sys
N = int(sys.stdin.readline().rstrip())
d = [0, 1, 3] + [0] * (N - 2)
for i in range(3,N+1):
    d[i] = d[i - 1] + 2*d[i - 2]
print(d[N] % 10007)
# n=2일 때  2*1타일을 | 1*2 타일 두 개 놓은 것을 = 2*2타일을 ㅁ이라고하면
# ||, =, ㅁ이므로 총 3