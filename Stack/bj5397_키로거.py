""" 다른 사람 풀이(스택 이용 풀이)
def solve():
  logger = input()

  l, r = [], []
  for i in range(len(logger)):
    if logger[i]=='<':
      if len(l)>0: r.append(l.pop())
    elif logger[i]=='>':
      if len(r)>0: l.append(r.pop())
    elif logger[i]=='-':
      if len(l)>0: l.pop()
    else:
      l.append(logger[i])
  print(''.join(l)+''.join(reversed(r)))

for _ in range(int(input())):
  solve()
"""
# deque이용한 내 풀이
import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

T = int(input())
for test in range(T):
    cursor_l = deque()
    cursor_r = deque()
    for i in input():
        if i == '<':
            if cursor_l:
                cursor_r.appendleft(cursor_l.pop())
        elif i == '>':
            if cursor_r:
                cursor_l.append(cursor_r.popleft())
        elif i == '-':
            if cursor_l:
                cursor_l.pop()
        else:
            cursor_l.append(i)
    print(''.join(cursor_l+cursor_r))