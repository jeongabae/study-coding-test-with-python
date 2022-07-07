# N = int(input())
# num = list(map(int, input().split()))
# for i in num:
#     if i == 1:
#         N -= 1
#     for j in range(2, i):
#         if i % j == 0:
#             N -= 1
#             break
# print(N)
"""짧은 다른분 풀이

print(sum(all(i%j for j in range(2,i))*i>1 for i in map(int,input().split())))

이걸 풀어쓰면
input()

s = []
for i in map(int, input().split()): #1 4 5 7 인 경우
    a = all(i%j for j in range(2,i))*i>1 # False False True True가 나옴. (i>1인 i에 대해 소수 검사를 했을 때 i%j==0이 안나오면 True)
    s.append(a)
print(sum(s)) #True(1)의 합은 2
"""
