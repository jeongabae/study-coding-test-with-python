def solution(my_string):
    ans = ''
    for i in my_string:
        if i.isupper():
            ans+=i.lower()
        else:
            ans+=i.upper()
    return ans

"""swapcase()
def solution(my_string):
    return my_string.swapcase()
"""

"""숏코딩한거
def solution(my_string):
    return ''.join([x.lower() if x.isupper() else x.upper() for x in my_string])
"""