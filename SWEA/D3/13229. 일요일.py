T = int(input())
dic = {'MON': 6, 'TUE': 5, 'WED': 4, 'THU': 3, 'FRI': 2, 'SAT': 1, 'SUN': 7}
for test_case in range(1, T + 1):
    day = input()
    print(f'#{test_case} {dic[day]}')