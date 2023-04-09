def solution(n):
    i=2
    prime = set()
    while i<=n:
        if n%i==0:
            prime.add(i)
            n//=i
        else:
            i+=1
    return sorted(list(prime))

"""다른 분 풀이
def solution(n):
    answer = []
    d = 2
    while d <= n:
        if n % d == 0:
            n /= d
            if d not in answer:
                answer.append(d)
        else:
            d += 1
    return answer
"""