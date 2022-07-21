E, S, M = map(int, input().split())
year = 1

while 1:
    if (E-year)%15==0 and (S-year)%28==0 and (M-year)%19==0:
        break
    year+=1

print(year)