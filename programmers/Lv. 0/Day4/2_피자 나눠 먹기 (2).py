def solution(n):
    for i in range(1,n+1):
        if i*6%n==0:
            return i

"""피자 개수 이용
def solution(n):
    pizza = 1
    while(pizza*6)%n!=0:
        pizza+=1
    return pizza
"""

"""피자 조각 수 이용
def solution(n):
    pizza = 6
    while pizza%n!=0:
        pizza+=6
    return pizza/6
"""