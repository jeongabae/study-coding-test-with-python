def solution(hp):
    jangoon = hp//5
    byeong = (hp%5)//3
    il = (hp%5)%3
    return jangoon+byeong+il


"""신박 풀이
def solution(hp):
    answer = 0
    for ant in [5, 3, 1]:
        d, hp = divmod(hp, ant)
        answer += d
    return answer
    """