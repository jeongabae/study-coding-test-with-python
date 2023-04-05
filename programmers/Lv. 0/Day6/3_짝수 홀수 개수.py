def solution(num_list):
    return [len([n for n in num_list if n%2==0]),len([n for n in num_list if n%2])]
"""굳 아이디어
def solution(num_list):
    answer = [0,0]
    for n in num_list:
        answer[n%2]+=1
    return answer
"""