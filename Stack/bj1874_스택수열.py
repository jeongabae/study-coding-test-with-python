import sys
def input():
    return sys.stdin.readline().rstrip()

n = int(input())
num = [int(input()) for _ in range(n)]
m, s, op = 1, [], [] #m이 1인 이유는 스택에 1부터 쌓을 것이기 때문에(문제에 수열을 이루는 1이상 n이하의 정수가 하나씩 순서대로 주어진다함)
                    #s는 사용할 스택
                    #op에는 +(push)를 했는지 -(pop)을 했는 지 저장

for i in num:
    while not s or s[-1] < int(i):
        op.append('+')
        s.append(m)
        m += 1
    if s[-1] > int(i): #스택에 마지막으로 넣은 원소(s[-1])가 i(수열을 이뤄야하는 수)보다 크게 되면
                      # 스택 특정 상 더 작은 수를 먼저 꺼낼 수 없으므로 수열을 못 만드는 것.
        print('NO')
        exit() #break를 쓰게 되면 NO만 출력되는게 아니라 다시 반복문 돌아서 딴 것도 출력.. exit()혹은 exit(0)으로 써줘야 한다
    else:#스택에 마지막으로 넣은 원소(s[-1])가 i(수열을 이뤄야하는 수)보다 크지 않으면 이번에 pop할 숫자 = i 일 것이므로 pop해줌.
        op.append('-')
        s.pop()

print('\n'.join(op))
"""예제 이해
입력
8
4
3
6
8
7
5
2
1

출력
+
+
+
+
-
-
+
+
-
+
+
-
-
-
-
-

설명
1234 : ++++ 4까지 push
12 : -- 4 pop 3 pop
1256 : ++ 5,6 push
125 : - 5 pop
12578 : ++ 7,8 push
125 : -- 8 pop 7 pop
: 5 pop 2 pop 1 pop
이런식으로하면
출력이 위와 같이 나온다!
"""