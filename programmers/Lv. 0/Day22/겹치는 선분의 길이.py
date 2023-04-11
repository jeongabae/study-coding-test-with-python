def solution(lines):
    l = [set(range(min(i), max(i))) for i in lines]
    return len(l[0] & l[1] | l[0] & l[2] | l[1] & l[2])