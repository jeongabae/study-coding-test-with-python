T = int(input())
for t in range(1, T + 1):
    a, b = map(int, input().split())
    ans = ''
    if a < b:
        ans = '<'
    elif a > b:
        ans = '>'
    else:
        ans = '='
    print('#{} {}'.format(t, ans))