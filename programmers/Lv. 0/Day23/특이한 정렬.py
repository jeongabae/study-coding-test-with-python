def solution(numlist, n):
    numlist.sort(key = lambda x : (abs(n-x), n-x))
    return numlist