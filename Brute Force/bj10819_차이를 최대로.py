from itertools import permutations

N = int(input())
nums = list(map(int, input().split()))
ans = 0


def find_max(arr):  #주어진 식의 최대를 찾기 위함
    global ans

    tmp = 0 #원소들의 차의 절대값을 더한 최대값를 저장
    for i in range(len(arr) - 1):
        tmp += abs(arr[i] - arr[i + 1]) #배열의 원소의 차의 절대값을 더해준다.
    ans = max(ans, tmp) #비교해서 최대값을 저장


for i in permutations(nums): #permutations라이브러리 이용(입력받은 리스트의 원소중에서 N개를 뽑는다.)
    find_max(i) #각각의 순열마다 원소들의 차의 절대값의 최대값을 구하는 함수

print(ans)

"""
#내풀이 2 : 라이브러리 함수 쓰는 것 보단 느리지만 164ms
n = int(input())
nums = list(map(int, input().split()))
nums.sort()
ans = 0
def find_max(arr):  #주어진 식의 최대를 찾기 위함
    global ans

    tmp = 0 #원소들의 차의 절대값을 더한 최대값를 저장
    for i in range(len(arr) - 1):
        tmp += abs(arr[i] - arr[i + 1]) #배열의 원소의 차의 절대값을 더해준다.
    ans = max(ans, tmp) #비교해서 최대값을 저장

def next_permutations(a): #다음 순열 구하는 함수
    find_max(a) # 다음 순열 찾기 전에 주어진 식의 최대 값 구해줌
    # 1. a[i-1] < a[i]를 만족하는 가장 큰 i를 찾는다.
    i = n - 1
    while (a[i - 1] >= a[i] and i > 0):  # a[i-1] < a[i]를 만족하지 않는 경우 즉,a[i-1]>=a[i] 그리고 i<0이면 그 전 인덱스 확인.
        i -= 1

    # i<=0이 되면 다 내림차순이란 소리..!(즉 맨 마지막 순열)
    if i <= 0:
        return -1

    # 2. i<=j이면서 a[i-1]<a[j]를 만족하는 가장 큰 j를 찾는다.
    else:
        j = n - 1
        while (a[i - 1] >= a[j]):
            j -= 1

        # 3. a[i-1]과 a[j]를 swap한다.(바꿔준다.)
        a[i - 1], a[j] = a[j], a[i - 1]

        # 4. i번째의 값부터 그 이후 값 모두를 오름차순 정렬
        sort_from_jth_of_a = a[i:]
        sort_from_jth_of_a.sort()
        ans = a[:i] + sort_from_jth_of_a

        return ans

while 1:
    nums = next_permutations(nums)
    if nums==-1:
        break

print(ans)
"""
"""내풀이3 : 백트래킹 이용 (제일 느린 풀이)
n = int(input())
nums = list(map(int, input().split()))
temp = [] #0~n-1개로 순열 만든거 저장
ans = [] #최대값 저장

def dfs():
    if len(temp) == n:
        ans.append(sum(abs(nums[temp[i + 1]] - nums[temp[i]]) for i in range(n - 1)))
        return
    for i in range(n):
        if i not in temp:
            temp.append(i)
            dfs()
            temp.pop()

dfs()
print(max(ans))
"""