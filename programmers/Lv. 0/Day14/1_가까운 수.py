def solution(array, n):
    array.sort() #이거 없으면 틀림!!
    a=[]
    for i in array:
        a.append(abs(i-n))
    return array[a.index(min(a))]

"""쿨한 풀이. 람다 이용!
solution=lambda a,n:sorted(a,key=lambda x:(abs(x-n),x))[0]
"""

"""풀이2
def solution(array, n):
    array.sort(key = lambda x : (abs(x-n), x-n))
    answer = array[0]
    return answer
"""