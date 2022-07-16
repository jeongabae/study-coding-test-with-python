import sys
def input():
    return sys.stdin.readline().rstrip()

N = int(input())
arr=[1,2,4]
T = [int(input()) for i in range(N)]

for i in range(4,max(T)+1):
    arr.append(sum(arr[-3:])%1000000009)
for x in T:
    print(arr[x-1])
"""
n=1일때 d[0] = 1 #1
n=2일때 d[1] = 2 #2, 1+1
n=3일때 d[2] = 4 #3, 1+2, 2+1, 1+1+1
"""

"""다른분 풀이
import sys
input = sys.stdin.readline

list_sum = [0] * 1000001
list_sum[1] = 1
list_sum[2] = 2
list_sum[3] = 4

for i in range(4, 1000001):
    list_sum[i] = list_sum[i-1] + list_sum[i-2] + list_sum[i-3]
    list_sum[i] %= 1000000009

T = int(input())
for j in range(T):
    n = int(input())
    print(list_sum[n])
    """