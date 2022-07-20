import sys

while True:
    s = sys.stdin.readline().rstrip()
    if s=='.': break
    stack = []
    no = 0

    for c in s:
        if c == '(' or c == '[': stack.append(c)
        elif c == ')':
            if not stack or stack[-1]=='[':
                no+=1
                break
            elif stack[-1]== '(':
                stack.pop()
        elif c == ']':
            if not stack or stack[-1]=='(':
                no+=1
                break
            if stack[-1]=='[':
                stack.pop()

    print("no" if no or len(stack) else "yes")

""" 내 풀이보다 빠른 풀이
from sys import stdin, stdout

def isvalid(s):
    stack = []
    for c in s:
        if c in '([':
            stack.append(c)
        elif c == ')':
            if not stack or stack.pop() != '(':
                return False
        elif c == ']':
            if not stack or stack.pop() != '[':
                return False
    return not stack

strings = stdin.readlines()
strings.pop()
for string in strings:
    stdout.write("yes\n" if isvalid(string) else "no\n")
"""