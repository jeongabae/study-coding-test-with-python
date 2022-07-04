n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1
for x in data:
    # 만들 수 없는 금액을 찾았을 때 반복 종료
    if target < x:
        break
    target += x

# 만들 수 없는 금액 출력
print(target)
"""예시
5
3 2 1 1 9를 넣으면
[1,1,2,3,9]로 정렬 후 확인
1(target) = 1이므로 1+1=2(target)
2(target) > 1이므로 2+1=3(target)
3(target) > 2이므로 3+2=5(target)
5(target) > 3이므로 5+3=8(target)
8(target) < 9이므로 break target = 8
"""