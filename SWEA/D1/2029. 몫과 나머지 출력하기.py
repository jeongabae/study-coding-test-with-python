# import sys
# sys.stdin = open("/Users/jeongabae/PycharmProjects/study-coding-test-with-python/SWEA/input (2).txt", "r")

T = int(input())
for t in range(1, T + 1):
    a, b = map(int, input().split())
    print('#{} {} {}'.format(t, a//b, a%b))