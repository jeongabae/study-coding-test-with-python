def solution(arr):
    answer = [arr[0]]
    for i in range(1,len(arr)):
        if arr[i-1]!=arr[i]:
            answer.append(arr[i])
    return answer

"""
def solution(arr):
    a = []
    for i in arr:
        if a[-1:] == [i]: continue #[-1]을 통해 비교하면 empty array일 때 인덱싱오류가나서 [-1:]를 통해 리스트를 만들어 비교
        a.append(i)
    return a
"""