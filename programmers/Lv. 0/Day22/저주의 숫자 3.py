def solution(n):
    num = 0
    for i in range(n):
        num+=1
        while not num%3 or '3' in str(num):
            num+=1
    return num