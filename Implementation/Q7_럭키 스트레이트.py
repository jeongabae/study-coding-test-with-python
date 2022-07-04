n = input()
length = len(n) # 점수 값의 총 자릿수
summary = 0

# 왼쪽 부분의 자릿수의 합 더하기
for i in range(length // 2):
    summary += int(n[i])

# 오른쪽 부분의 자릿수의 합 빼기
for i in range(length // 2, length):
    summary -= int(n[i])

# 왼쪽 부분과 오른쪽 부분의 자릿수 합이 동일한지 검사
if summary == 0:
    print("LUCKY")
else:
    print("READY")
"""내 풀이
n = input()
s = []
for i in n:
    s.append(int(i))
middle = len(s)//2
print("LUCKY" if sum(s[0:middle])==sum(s[middle:]) else "READY")
"""
"""다른 분 풀이
n=input()
d=len(n)//2
print("LUCKY"if sum(map(int, n[:d]))==sum(map(int, n[d:]))else"READY")
"""