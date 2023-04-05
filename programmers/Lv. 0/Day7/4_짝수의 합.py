def solution(n):
    a = n//2
    return a*(a+1)
#cf) 홀수 n 개를 합치면 그 합은 n 의 제곱
#cf) 짝수 n 개를 합치면 그 합은 n×(n+1)
"""
def solution(n):
    return sum([i for i in range(2, n + 1, 2)])
"""