T = int(input())
for test_case in range(1, T+1):
    m, d = map(int, input().split())
    month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = [3, 4, 5, 6, 0, 1, 2]
    index = (sum(month[:m]) + d) % 7
    print(f"#{test_case} {day[index]}")