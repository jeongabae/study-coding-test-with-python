def solution(my_string):
    for i in 'aeiou':
        my_string = my_string.replace(i,"")
    return my_string


"""모음을 제거한다는 생각말고 모음 아닌걸 붙인다는 관점으로 푼 풀이
def solution(my_string):
    return "".join([i for i in my_string if not(i in "aeiou")])
"""