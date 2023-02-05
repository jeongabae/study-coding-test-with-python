import sys
def input():
    return sys.stdin.readline().rstrip()

def binarysearch(start,end,X,arr):
    while (start <= end):
        mid = (start + end) // 2
        if arr[mid] == X:
            return "yes"
        else:
            if arr[mid] > X:
                end = mid - 1
            else:
                start = mid + 1
    return "no"

N = int(input())
arr = list(map(int, input().split()))
arr.sort()
M = int(input())
arr2 = list(map(int, input().split()))
for i in range(M):
    print(binarysearch(0,N-1,arr2[i],arr),end=" ")
