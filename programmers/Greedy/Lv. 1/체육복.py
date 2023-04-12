def solution(n, lost, reserve):
    num = [1] * n

    for i in lost:
        num[i - 1] -= 1
    for j in reserve:
        num[j - 1] += 1

    for k in range(n):
        if num[k] == 0:
            if k - 1 >= 0 and num[k - 1] > 1:
                num[k - 1] -= 1
                num[k] += 1
                continue
            elif k + 1 < n and num[k + 1] > 1:
                num[k + 1] -= 1
                num[k] += 1
                continue

    return n - num.count(0)


"""
def solution(n, lost, reserve):
    reserve2 = set(reserve) - set(lost)
    lost2 = set(lost) - set(reserve)
    
    for student in reserve2:
        if (student - 1) in lost2:
            lost2.remove(student - 1)
        elif (student + 1) in lost2:
            lost2.remove(student + 1)
            
    return n - len(lost2)
"""