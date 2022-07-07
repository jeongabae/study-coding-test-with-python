# n = int(input())
# fac = 1
# cnt = 0
# while n!=0:
#     fac = fac * n
#     n -= 1
# fac = str(fac)
# for i in range(len(fac)-1,0,-1):
#     if fac[i]!='0':
#         break
#     else:
#         cnt+=1
# print(cnt)
"""함수가 이미 있넹...?
from math import factorial
n = int(input())
cnt = 0
for x in str(factorial(n))[::-1]:
    if x != '0':
        break
    cnt += 1
print(cnt)
"""
"""제일 좋은 풀이
팩토리얼로 얻을 수 있는 수를 인수 분해 하면,
0이 생기는 때는 2x5=10이 곱해질 때이므로 따라서 5의 개수를 찾으면 쉽다. 
N = int(input())
print(N//5 + N//25 + N//125) #N의 범위(0<N<500)이므로 625는 500 범위 밖이니 제외.
"""