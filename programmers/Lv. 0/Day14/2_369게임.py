def solution(order):
    return len([1 for i in str(order) if i in "369"])

"""
def solution(order):
    ans = 0
    for i in '369':
        ans += str(order).count(i)
    return ans
"""

"""람다 이용 풀이
def solution(order):
    return sum(map(lambda x: str(order).count(str(x)), [3, 6, 9]))
"""