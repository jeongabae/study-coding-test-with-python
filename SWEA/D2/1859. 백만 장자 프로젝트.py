# T = int(input())
# for test_case in range(1, T+1):
#     n = int(input())
#     prices = list(map(int, input().split()))
#     sell_price = [0]*n
#     max_price = prices[-1]
#
#     for i in range(n-1, -1, -1):
#         max_price = max(max_price, prices[i])
#         sell_price[i] = max_price
#
#     max_profit = 0
#     for p, sell_p in zip(prices, sell_price):
#         profit = sell_p - p
#         if profit > 0:
#             max_profit += profit
#     print(f'#{test_case} {max_profit}')

# 다른 풀이1
# T = int(input())
# for test_case in range(1, T+1):
#     n = int(input())
#     lst = list(map(int, input().split()))
#
#     ans = s = 0
#     while s<n:
#         i_max = s
#         for i in range(s+1, n):
#             if lst[i_max] < lst[i]:
#                 i_max = i
#         for i in range(s, i_max):
#             ans += (lst[i_max] - lst[i])
#         s = i_max + 1
#     print(f'#{test_case} {max_profit}')

#다른 풀이2
T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    price = list(map(int, input().split()))[::-1]
    ans = max_price = 0
    for i in price:
        if max_price < i:
            max_price = i
        else:
            ans += (max_price-i)
    print(f'#{test_case} {ans}')