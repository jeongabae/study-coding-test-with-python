import sys
s = list(sys.stdin.readline().rstrip())

stack = []
value = 0
cal = 1

for i in range(len(s)):

    if s[i] in "([":
        stack.append(s[i])
        cal *= 2 if s[i] == '(' else 3
        #print("경우1 tmp", cal, "ans", value, "stack", stack)

    elif s[i] == ")":
        if not stack or stack[-1] == "[":
            print(0)
            #print("경우2 tmp", cal, "ans", value, "stack", stack)
            exit()
        if s[i - 1] == "(":
            value += cal  # 괄호가 바로 닫히는 경우만 더해줌 ()
        stack.pop()
        cal //= 2
        #print("경우3 tmp", cal, "ans", value, "stack", stack)


    else:
        if not stack or stack[-1] == "(":
            print(0)
            #print("경우4 tmp", cal, "ans", value, "stack", stack)
            exit()
        if s[i - 1] == "[": # 괄호가 바로 닫히는 경우만 더해줌 []
            value += cal

        stack.pop()
        cal //= 3
        #print("경우5 tmp", cal, "ans", value, "stack", stack)

print(0 if stack else value)
"""실패한 내 또 다른 풀이..^^
import sys
s=sys.stdin.readline().rstrip()
s=s.replace("()",'2').replace("[]",'3').replace("(",'+2*(').replace("[",'+3*[').replace('[','(').replace(']',')')
try:print(eval(s))
except:print(0)
# 추가 : .replace('[','(').replace(']',')')대신 .replace(']','][0]')으로 바꾸면 되는데 왜 되는진 모름.
"""

"""다른 사람의 재귀함수 이용 풀이
import sys
input = sys.stdin.readline

s = list(input().rstrip())[::-1]

def cal(start):
    r = 0
    while s:
        a = s.pop()
        if a == "(" or a == "[":
            r += cal(a)
        elif start == "(" and a == ")":
            return 2 * max(1,r)
        elif start == "[" and a == "]":
            return 3 * max(1,r)
    
    # 리스트가 비었는데 최종 return 하지 못했다는 것은 괄호에 문제가 있음을 의미
    print(0)
    sys.exit()

ans = 0    
while s:
    ans += cal(s.pop())
print(ans)
"""

"""다른 사람 eval 이용 풀이
s=str.replace
try:print(eval(s(s(s(s(s(input(),'()','+2'),'[]','+3'),'(','+2*('),'[','+3*['),']','][0]')))
except:print(0)
"""