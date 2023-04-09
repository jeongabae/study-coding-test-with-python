def solution(n):
    answer = 0
    for i in range(n + 1):
        c = 0
        for j in range(1, i + 1):
            if i % j == 0:
                c += 1
        if c >= 3:
            answer += 1

    return answer

"""제일 좋은 풀이 : 최소한의 카운트만 함
def solution(n):
    output = 0
    for i in range(4, n + 1): #0~3까지는 소수라 뺌
        for j in range(2, int(i ** 0.5) + 1): 
            if i % j == 0:
                output += 1 #1, 그리고 j와 대칭인 수, 그리고 j까지 세 개가 약수이므로
                break
    return output
"""