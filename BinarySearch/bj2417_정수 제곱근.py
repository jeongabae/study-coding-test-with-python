#[Binary Search] 백준 2417번 : 정수 제곱근
n=int(input())
start=0 #start=0, end=n이라 두고 이분탐색 진행
end=n
while start<=end:
    mid=(start+end)//2
    if mid**2==n:
        start=mid
        break
    elif mid**2<n:
        start=mid+1
    else:
        end=mid-1
print(start)