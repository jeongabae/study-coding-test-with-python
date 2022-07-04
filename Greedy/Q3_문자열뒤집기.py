data = input()
count0 = 0 # 전부 0으로 바꾸는 경우
count1 = 0 # 전부 1로 바꾸는 경우

# 첫 번째 원소에 대해서 처리
if data[0] == '1':
    count0 += 1
else:
    count1 += 1

# 두 번째 원소부터 모든 원소를 확인하며
for i in range(len(data) - 1):
    if data[i] != data[i + 1]:
        # 다음 수에서 1로 바뀌는 경우
        if data[i + 1] == '1':
            count0 += 1
        # 다음 수에서 0으로 바뀌는 경우
        else:
            count1 += 1

print(min(count0, count1))
"""나는 조금 다르게 푼...!
s = input()
change = 0
for i in range(len(s)-1):
    if s[i]!=s[i+1]:
        change += 1
print((change+1)//2)
#예를 들어 1100110 이면 0->1 또는 0->1로 바꾸니 횟수는 3번 (3+1)//2 = 2가 최소 횟수.
"""
