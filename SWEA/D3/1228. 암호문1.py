# import sys
# sys.stdin = open("input_1228.txt", "r")

for test_case in range(1, 11):
    n = int(input())
    arr = list(map(int, input().split()))
    m = int(input())
    cmd = input().split()

    i = 0
    while i < len(cmd):
        c = cmd[i]
        if c == 'I':
            x = int(cmd[i+1])
            y = int(cmd[i+2])
            s = list(map(int, cmd[i+3:i+3+y]))
            arr[x:x] = s
            i += 3 + y
        else:
            i += 1

    ans = arr[:10]
    print(f'#{test_case}', *ans)