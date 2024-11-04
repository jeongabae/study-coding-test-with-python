T = int(input())
for test_case in range(1, T + 1):
    dir = input()
    a = b = 1
    for i in dir:
        if i=='L':
            b+=a
        else:
            a+=b
    print(f'#{test_case} {a} {b}')