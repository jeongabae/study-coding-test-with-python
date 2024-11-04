for test_case in range(1, 11):
    num = int(input())
    arr = list(map(int, input().split()))
    cycle = 1
    while True:
        p = arr.pop(0) - cycle
        if p <= 0:
            arr.append(0)
            break
        else:
            arr.append(p)

        cycle += 1
        if cycle > 5:
            cycle = 1

    print(f'#{test_case}', *arr)