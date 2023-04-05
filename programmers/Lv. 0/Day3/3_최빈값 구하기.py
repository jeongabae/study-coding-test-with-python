from collections import Counter
def solution(array):
    cnt = Counter(array).most_common()
    max_num = cnt[0][1]

    for num in cnt[1:]:
        if num[1] == max_num:
            return -1
    return cnt[0][0]
#내풀이보다 아래꺼 참고

"""신박한 다른 사람 풀이
def solution(array):
    while len(array) != 0:
        for i, a in enumerate(set(array)):
            array.remove(a)
        if i == 0: return a
    return -1
"""
"""다른 사람 풀이
from collections import Counter

def solution(array):
    a = Counter(array).most_common(2)
    if len(a) == 1:
        return a[0][0]
    if a[0][1] == a[1][1]:
        return -1
    return a[0][0]
"""