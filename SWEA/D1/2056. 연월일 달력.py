T = int(input())
for test_case in range(1, T + 1):
    a = input()
    y, m, d = int(a[:4]), int(a[4:6]), int(a[6:])
    ans = True
    if m<1 or m>12:
        ans = False
    else:
        if m in (1, 3, 5, 7, 8, 10, 12):
            if d < 1 or d > 31:
                ans = False
        elif m in (4, 6, 9, 11):
            if d < 1 or d > 30:
                ans = False
        else:
            if d<1 or d>28:
                ans = False
    print('#{} {}'.format(test_case, a[:4]+'/'+a[4:6]+'/'+a[6:] if ans else -1))

# 다른 사람 풀이 참고해서 짠 풀이#코드는 짧지만 실행시간이 아주 살짝 더 걸림 그래도 참고!
# T = int(input())
# days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
# for test_case in range(1, T + 1):
#     case = input()
#     y, m, d = case[0:4], case[4:6], case[6:]
#
#     answer = ''
#     if 0 < int(m) < 13 and 0 < int(d) <= days[int(m)]:
#         answer = y + '/' + m + '/' + d
#     else:
#         answer = '-1'
#     print("#{} {}".format(test_case, answer))