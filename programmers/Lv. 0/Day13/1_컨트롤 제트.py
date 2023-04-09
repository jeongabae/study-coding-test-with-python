def solution(s):
    a = s.split()
    a_sum = 0
    for i in range(len(a)):
        a_sum -= int(a[i-1]) if a[i]=='Z' else -int(a[i])
    return a_sum

""" s:=~~이부분만 다르고 다 똑같음.
def solution(s):
    answer = 0
    for i in range(len(s := s.split(" "))):
        answer += int(s[i]) if s[i] != "Z" else -int(s[i-1])
    return answer
"""