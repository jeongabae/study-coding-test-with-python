#10972 다음 순열과 부등호 반대
"""
a=[num1, num2, num3, num4...] 의 이전 순열을 찾기 위해서는
1. a[i-1] > a[i]를 만족하는 가장 큰 i를 찾는다. #i<=0이 되면 다 내림차순이란 소리..!(즉 맨 마지막 순열)
2. i<=j이면서 a[i-1]>a[j]를 만족하는 가장 큰 j를 찾는다.
3. a[i-1]과 a[j]를 swap한다.(바꿔준다.)
4. i번째의 값부터 그 이후 값 모두를 내림차순 정렬

ex) a=[1,2,4,3]의 이전 순열? [1,2,3,4]
1. a[i-1] > a[i]를 만족하는 i는 3이므로 가장 큰 i는 3
2. 3<=j이면서 a[2]>a[j]를 만족하는 j는 3뿐.
3. a[i-1=2]와a[j=3]의 값을 서로 바꿔주면 [1,2,3,4]
4. i=3이므로 a[3]이후의 값들을 내림차순 정렬해줘야하는데 3이 마지막 인덱스 값이므로 정렬 없이 [1,2,3,4]이 답.
"""
import sys
def input():
    return sys.stdin.readline().rstrip()

n=int(input())
a=[int(i) for i in input().split()]

#1. a[i-1] > a[i]를 만족하는 가장 큰 i를 찾는다.
i = n-1
while(a[i-1]<=a[i] and i>0): #a[i-1] < a[i]를 만족하지 않는 경우 즉,a[i-1]>=a[i] 그리고 i<0이면 그 전 인덱스 확인.
    i-=1

#i<=0이 되면 다 오름차순이란 소리..!(즉 맨 처음 순열)
if i<=0:
    print(-1)

#2. i<=j이면서 a[i-1]>a[j]를 만족하는 가장 큰 j를 찾는다.
else:
    j = n-1
    while(a[i-1]<=a[j]):
        j -= 1

    #3. a[i-1]과 a[j]를 swap한다.(바꿔준다.)
    a[i-1],a[j] = a[j], a[i-1]

    #4. i번째의 값부터 그 이후 값 모두를 내림차순 정렬
    sort_from_jth_of_a = a[i:]
    sort_from_jth_of_a.sort(reverse=True)
    ans = a[:i] + sort_from_jth_of_a

    #출력
    print(*ans)
"""내 알고리즘이랑 똑같은 다른 사람(1등) 코드 : 구현 방식에서만 약간 차이 있음.
def pre_permutation(n, a):
    i = n-1
    while i > 0 and a[i-1] <= a[i]: # A[i-1] < A[i] 를 만족하는 가장 큰 i를 찾는다
        i -=1
    if i <= 0 : return False       # 마지막 순열
    j = n -1
    while a[j] >= a[i-1]: # j ≥ i 이면서 A[j] > A[i-1] 를 만족하는 가장 큰 j를 찾는다
        j -= 1
    a[i-1],a[j] = a[j],a[i-1]
    j = n-1
    while i < j:
        a[i],a[j] = a[j],a[i]
        i += 1
        j -= 1
    return True

n = int(input())
a = list(map(int, input().split()))
if pre_permutation(n, a):
    print(' '.join(map(str,a)))
else:
    print(-1)
    """