import math 

def solution(balls, share):
    return math.comb(balls, share)

"""cf 팩토리얼 함수 직접 써서(팩토리얼 함수도 사실 math.factorial(x) 쓰면 됨) 조합 구하는 긴 방법..
def solution(balls, share):
    answer = factorial(balls) / (factorial(balls - share) * factorial(share))
    return answer

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result
"""