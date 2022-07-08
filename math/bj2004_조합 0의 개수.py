n, m = map(int, input().split())
def cnt2or5(a,b):
    cnt = 0 #5또는 2의 개수 카운트 (소인수 분해하면..)
    while a > 0:
        cnt += a//b
        a //= b
    return cnt

cnt5 = cnt2or5(n, 5) - cnt2or5(m, 5) - cnt2or5(n - m, 5)
cnt2 = cnt2or5(n, 2) - cnt2or5(m, 2) - cnt2or5(n - m, 2)
print(min(cnt5, cnt2))

"""
만약에 10C5이면 10!/{(10-5)!5!}이므로
cnt5 = cnt2or5(n, 5) - cnt2or5(m, 5) - cnt2or5(n - m, 5)
cnt2 = cnt2or5(n, 2) - cnt2or5(m, 2) - cnt2or5(n - m, 2)
을 해주는 것!
"""