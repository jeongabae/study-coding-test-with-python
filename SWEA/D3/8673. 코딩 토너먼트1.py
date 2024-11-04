T = int(input())
for test_case in range(1, T + 1):
    k = int(input())
    arr = list(map(int, input().split()))
    bored = 0

    while k>0:
        next_round = []
        for i in range(0, len(arr), 2):
            player1, player2 = arr[i], arr[i+1]
            b = abs(player1-player2)
            bored += b
            next_round.append(max(player1, player2))

        arr = next_round
        k-=1

    print(f'#{test_case} {bored}')