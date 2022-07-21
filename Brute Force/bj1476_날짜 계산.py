E, S, M = map(int, input().split())
year = 1

while 1:
    if (E-year)%15==0 and (S-year)%28==0 and (M-year)%19==0:
        break
    year+=1

print(year)
"""
### 중국인의 나머지 정리 이용한 빠른 풀이 참고 : https://passwd.tistory.com/entry/BOJ-1476-%EB%82%A0%EC%A7%9C-%EA%B3%84%EC%82%B0
e,s,m = map(int, input().split())
x = (6916*e+4845*s+4200*m) % 7980
print(x if x else 7980)
"""