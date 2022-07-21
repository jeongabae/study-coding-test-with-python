#3040풀고 다시 풀어본
from itertools import combinations as c
l=sorted(int(input())for i in range(9))
for i in c(l,7):
    if(sum(i)==100):
        for j in i:print(j)
        break