for test_case in range(1, 11):
    num = int(input())
    arr = [list(input()) for _ in range(8)]
    arr2 = list(zip(*arr))
    ans = 0

    for i in range(8):
        for j in range(8-num+1):
            chk = arr[i][j:j+num]
            chk2 = arr2[i][j:j+num]
            if chk == chk[::-1]:
                ans += 1
            if chk2 == chk2[::-1]:
                ans += 1

    print(f'#{test_case} {ans}')