def solution(n):
    return len([num for num in range(1, n+1) if n%num == 0])

"""숏코딩 말고는 대충 이케 풀 수 있음
def solution(n):
    answer =0 
    for i in range(n):
        if n % (i+1) ==0:
            answer +=1
    return answer
"""