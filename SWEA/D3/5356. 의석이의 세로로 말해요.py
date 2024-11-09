T = int(input())
for test_case in range(1, T+1):
    arr = [list(input()) for _ in range(5)]
    arr2 = [''.join(x) for x in zip(*arr)]
    print(f'#{test_case} ', end='')
    for row in arr2:
        print(*row, end=' ')
    print()