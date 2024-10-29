# import sys
# sys.stdin = open("input_2068.txt", "r")
T = int(input())
for t in range(1, T + 1):
    print('#{} {}'.format(t, max(map(int, input().split()))))