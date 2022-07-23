import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
cnt = 0

for i in range(N):
    s = input()
    stack = []

    for i in s:
        if stack and stack[-1] == i: #스택에 1개 이상 들어있고, 마지막으로 넣은 원소가 i와 같을 때
            stack.pop() # 스택의 마지막 원소를 꺼낸다.
        else:
            stack.append(i) # 그 외 경우는 스택에 추가

    if not stack: #만약 모두 짝지어져서 스택에 원소가 남아있지 않으면 그건 좋은 단어!
        cnt += 1
print(cnt)

"""나랑 비슷한 코드
import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
ans = 0
for i in range(N):
    stack = []
    a = input()
    for i in a:
        if not stack:
            stack.append(i)
        else:
            if stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
    if not stack:
        ans += 1
print(ans)
"""
"""스택 이용하지 않은 1등 풀이
num_of_good_words = 0

for _ in range(int(input())):
	word, temp = input(), ""
	while word != temp:
		temp = word
		word = word.replace("AA", "").replace("BB", "")
	if not word:
		num_of_good_words += 1

print(num_of_good_words)
"""