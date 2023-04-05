def solution(my_string, n):
    return ''.join(i*n for i in my_string)

"""내 풀이2
def solution(my_string, n):
    a=""
    for i in my_string:
        a+=i*n
    return a
"""