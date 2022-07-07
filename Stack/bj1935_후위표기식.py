#내풀이 1
import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
s = input()
op = '+-*/'
stack = []
num = [int(input()) for i in range(N)]
A = ord('A') #하나의 문자를 인자로 받고 해당 문자에 해당하는 유니코드 정수를 반환
for i in s:
    if i not in op:
        stack.append(num[ord(i)-A])
    else:
        a = stack.pop()
        b = stack.pop()
        if i == '+':
            stack.append(b+a)
        elif i == '-':
            stack.append(b-a)
        elif i == '*':
            stack.append(b*a)
        else:
            stack.append(b/a)

print(format(stack[0], '.2f')) #print(f"{stack[0]:.2f}")도 같은 표현
"""내풀이2
import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
s = input()
op = '+-*/'
dic = {}
stack = []
num = deque([int(input()) for i in range(N)])

for i in s:
    if i not in dic and i not in op: #ABC*+DE/-입력이면 ABCDE에 대해서만!
                                    # #AA+A+요로케 들어왔으면 A한 번만 처리하면 되므로 if i not in dic조건 붙은 것!
        dic[i] = num.popleft()

for i in s:
    if i not in op:
        stack.append(dic[i])
    else:
        a = stack.pop()
        b = stack.pop()
        if i == '+':
            stack.append(b+a)
        elif i == '-':
            stack.append(b-a)
        elif i == '*':
            stack.append(b*a)
        else:
            stack.append(b/a)

print(format(stack[0], '.2f')) #print(f"{stack[0]:.2f}")도 같은 표현
"""
"""1등분 코드
from sys import stdin
read = lambda: stdin.readline().rstrip()

n = int(read())
st = read()
val = {chr(65+i): int(read()) for i in range(n)}
stack = []

for i in st:
    if i.isupper():
        stack.append(val[i])
    else:
        v = []
        for j in range(2):
            a = stack.pop()
            v.append(a)

        if i == '+': stack.append(v[1] + v[0])
        elif i == '-': stack.append(v[1] - v[0])
        elif i == '/': stack.append(v[1] / v[0])
        elif i == '*': stack.append(v[1] * v[0])

print('%.2f' % stack.pop())
"""

"""2등분 코드
n = int(input())
expr = input()
char_to_num = dict()
stack = []
char_ascii = ord("A")

for _ in range(n):
    num = int(input())
    char_to_num[chr(char_ascii)] = num
    char_ascii += 1

for e in expr:
    if e == "*" or e == "+" or e == "/" or e == "-":
        a2, a1 = stack.pop(), stack.pop()
        if e == "*":
            stack.append(a1*a2)
        elif e == "+":
            stack.append(a1+a2)
        elif e == "-":
            stack.append(a1-a2)
        else:
            stack.append(a1/a2)
    else:
        num = char_to_num[e]
        stack.append(num)

print(f"{stack[0]:.2f}")
"""