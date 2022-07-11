import sys
def input():
    return sys.stdin.readline().rstrip()

T = int(input())
d = [0, 1, 2, 4]
for i in range(4, 12):
    d.append(sum(d[-3:]))
for _ in range(T):
    N = int(input())
    print(d[N])
"""
d[1] = 1 #1
d[2] = 2 #2, 1+1
d[3] = 4 #3, 1+2, 2+1, 1+1+1
"""
"""1등 분 코드 0번 인덱스부터 쓰신 것 빼고는 나랑 같음.
N = int(input())
arr=[1,2,4]
for i in range(4,11):
    arr.append(sum(arr[-3:]))
for _ in range(N):
    T = int(input())
    print(arr[T-1])

"""