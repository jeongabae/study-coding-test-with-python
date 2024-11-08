T = int(input())
for test_case in range(1, T+1):
    k = int(input())
    arr = []
    for i in range(k):
        n = int(input())
        if n!=0:
            arr.append(n)
        else:
            arr.pop()
    print(f'#{test_case} {sum(arr)}')