# from itertools import permutations 을 사용하거나 재귀함수 사용 시 이 문제 풀기 위해 필요한 시간복잡도 계산 결과 N!이라서 시간 초과 날 수 밖에 없음 ㅠ
# 그래서 인도의 수학자 나라야나 판디타가 고안한 다음 순열을 찾는 알고리즘 이용! 이를 이용하면 다음 순열 구하는 시간 복잡도는 O(N)
"""
a=[num1, num2, num3, num4...] 의 다음 순열을 찾기 위해서는
1. a[i-1] < a[i]를 만족하는 가장 큰 i를 찾는다. #i<=0이 되면 다 내림차순이란 소리..!(즉 맨 마지막 순열)
2. i<=j이면서 a[i-1]<a[j]를 만족하는 가장 큰 j를 찾는다.
3. a[i-1]과 a[j]를 swap한다.(바꿔준다.)
4. i번째의 값부터 그 이후 값 모두를 오름차순 정렬

ex) a=[1,2,3,4]의 다음 순열? [1,2,4,3]
1. a[i-1] < a[i]를 만족하는 i는 1,2,3이므로 가장 큰 i는 3
2. 3<=j이면서 a[2]<a[j]를 만족하는 j는 3뿐.
3. a[i-1=2]와a[j=3]의 값을 서로 바꿔주면 [1,2,4,3]
4. i=3이므로 a[3]이후의 값들을 오름차순 정렬해줘야하는데 3이 마지막 인덱스 값이므로 정렬 없이 [1,2,4,3]이 답.
"""
import sys
def input():
    return sys.stdin.readline().rstrip()

n=int(input())
a=[int(i) for i in input().split()]

#1. a[i-1] < a[i]를 만족하는 가장 큰 i를 찾는다.
i = n-1
while(a[i-1]>=a[i] and i>0): #a[i-1] < a[i]를 만족하지 않는 경우 즉,a[i-1]>=a[i] 그리고 i<0이면 그 전 인덱스 확인.
    i-=1

#i<=0이 되면 다 내림차순이란 소리..!(즉 맨 마지막 순열)
if i<=0:
    print(-1)

#2. i<=j이면서 a[i-1]<a[j]를 만족하는 가장 큰 j를 찾는다.
else:
    j = n-1
    while(a[i-1]>=a[j]):
        j -= 1

    #3. a[i-1]과 a[j]를 swap한다.(바꿔준다.)
    a[i-1],a[j] = a[j], a[i-1]

    #4. i번째의 값부터 그 이후 값 모두를 오름차순 정렬
    sort_from_jth_of_a = a[i:]
    sort_from_jth_of_a.sort()
    ans = a[:i] + sort_from_jth_of_a

    #출력
    print(*ans)
"""다른 사람 코드 : 내꺼랑 알고리즘은 같음
import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))
i = n-1
while arr[i-1]>=arr[i] and 0<i:
    i-=1
if i==0:
    print(-1)
else:
    j = n-1
    while j>=i and arr[j]<=arr[i-1]:
        j-=1
    arr[i-1], arr[j] = arr[j], arr[i-1]
    j = n-1
    while i<j:
        arr[i],arr[j] = arr[j],arr[i]
        i+=1
        j-=1
    print(" ".join(map(str, arr)))
    """