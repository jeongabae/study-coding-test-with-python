# 이 문제는 구현 유형으로 분류 되어있지만. 가능한 경우의 수를 모두 탐색해보는 탐색방법인 '완전 탐색(브루트포스)' 유형으로도 분류
# H를 입력받기
h = int(input())

count = 0
for i in range(h+1): # 시
    for j in range(60): # 분
        for k in range(60): #초
            # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
            if '3' in str(i) + str(j) + str(k):
                count += 1
print(count)