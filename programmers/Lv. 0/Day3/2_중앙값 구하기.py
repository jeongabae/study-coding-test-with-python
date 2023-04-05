def solution(array):
    array.sort()
    return array[len(array)//2]


"""sorted() 이용 풀이
def solution(array):
    return sorted(array)[len(array) // 2]
"""