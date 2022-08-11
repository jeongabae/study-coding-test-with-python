"""내풀이1 : 백트래킹 이용
import sys
def input():
    return sys.stdin.readline().rstrip()

L, C = map(int,input().split())
arr = list(map(str,input().split()))
arr.sort() #암호를 이루는 알파벳이 암호에서 증가하는 순서로 배열되었을 것이라고 추측된다고 했으므로
pwd = []
def check(password): #최소 한 개의 모음(a, e, i, o, u)과 최소 두 개의 자음으로 구성되어 있는 지 확인
    mo = ja = 0
    for i in password:
        if i=='a' or i=='e'or i=='i'or i=='o'or i=='u':
            mo+=1
        else:
            ja+=1
    return mo>=1 and ja>=2

def dfs(start): #백트래킹 사용
    if len(pwd) == L:
        if check(pwd):
            print(''.join(pwd))
        return

    for i in range(start, C):
        if arr[i] in pwd:
            continue
        pwd.append(arr[i])
        dfs(i)
        pwd.pop()
dfs(0)
"""
# 내풀이 2 : 조합함수 이용 (이게 당연히 더 빠름)
import sys
from itertools import combinations
def input():
    return sys.stdin.readline().rstrip()

L, C = map(int,input().split())
arr = list(map(str,input().split()))
arr.sort() #암호를 이루는 알파벳이 암호에서 증가하는 순서로 배열되었을 것이라고 추측된다고 했으므로

def check(password): #최소 한 개의 모음(a, e, i, o, u)과 최소 두 개의 자음으로 구성되어 있는 지 확인
    mo = ja = 0
    for i in password:
        if i=='a' or i=='e'or i=='i'or i=='o'or i=='u':
            mo+=1
        else:
            ja+=1
    return mo>=1 and ja>=2

for i in combinations(arr,L): #arr 중에 L개 선택해서
    if check(i): #조건 만족하면 출력
        print(''.join(i))