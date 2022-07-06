import sys

def input():
    return sys.stdin.readline().rstrip()

left_st = list(input())
right_st = []
M = int(input())
for i in range(M):
    cmd = input().split()
    c = cmd[0]

    if c == "L": #아래 두 줄을 if c=="L" and left_st:로 줄일 수 있음.
        if left_st:
            right_st.append(left_st.pop())
    elif c == "D":
        if right_st:
            left_st.append(right_st.pop())
    elif c == "B":
        if left_st:
            left_st.pop()
    elif c == "P":
        left_st.append(cmd[1])
left_st.extend(reversed(right_st)) #이 두 줄을 print("".join(left_st)+"".join(right_st))으로 줄일 수 있음.
                                    # 여기서 reverse쓰면 만약에 right_st이 비어있는 경우 오류가 나기때문에 reversed써야함.
print(''.join(left_st))

"""2등분 코드
from sys import stdin
l = stdin.read().rstrip().split("\n")
txt_l = list(l[0])
txt_r = []
l = l[2:]

for o in l:
    if o[0] == "P":
        txt_l.append(o[2])
    elif o=="L" and txt_l:
            txt_r.append(txt_l.pop())
    elif o=="D" and txt_r:
            txt_l.append(txt_r.pop())
    elif o=="B" and txt_l:
            txt_l.pop()

print("".join(txt_l)+"".join(txt_r[::-1]))"""