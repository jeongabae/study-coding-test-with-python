def solution(numbers):
    s=sorted(numbers)
    return max(s[-1]*s[-2],s[0]*s[1])