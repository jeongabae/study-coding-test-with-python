def solution(my_string):
    a = ''
    for i in my_string:
        if i not in a:
            a+=i
    return a


"""깔끔 풀이
def solution(my_string):
    return ''.join(dict.fromkeys(my_string))
"""