T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    rock = list(map(int, input().split()))
    distance = [0]*n
    for i in range(n):
        distance[i] = abs(rock[i])
    min_dis = min(distance)
    ans = distance.count(min_dis)
    print(f'#{test_case} {min_dis} {ans}')