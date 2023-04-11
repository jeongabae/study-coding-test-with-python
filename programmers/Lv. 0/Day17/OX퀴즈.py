def solution(quiz):
    ans = []
    for i in range(len(quiz)):
        quiz_s = quiz[i].split('=')
        if eval(quiz_s[0])==int(quiz_s[-1]):
            ans.append("O")
        else:
            ans.append("X")
    return ans

"""
def valid(equation):
    equation = equation.replace('=', '==')
    return eval(equation)

def solution(equations):
    return ["O" if valid(equation) else "X" for equation in equations]
"""

"""eval 안쓴 풀이(현업에서는 eval 안쓰므로)
def solution(quiz):
    answer = []
    for q in quiz:
        L,R = q.split(' = ')
        a,op,b = L.split()
        if op=='+':
            result = 'O' if int(a)+int(b)==int(R) else 'X'
            answer.append(result)
        else:
            result = 'O' if int(a)-int(b)==int(R) else 'X'
            answer.append(result)
    return answer
"""