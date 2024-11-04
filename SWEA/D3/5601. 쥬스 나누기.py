T = int(input())
for test_case in range(1, T + 1):
    n = input()
    print(f'#{test_case}', end=' ')
    for i in range(int(n)):
        print('1/'+n,end=' ')
    print()