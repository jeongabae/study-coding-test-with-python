T = int(input())
for t in range(1, T + 1):
    a = list(map(int, input().split()))
    print('#{} {}'.format(t, sum(i for i in a if i%2!=0)))