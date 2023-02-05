array=[1,2,3,4,5]
start=0
end=len(array)-1
X=3
while(start<=end):
    mid = (start+end)//2
    if array[mid]==X:
        answer = mid
        break
    else:
        if array[mid]>X:
            end = mid-1
        else:
            start = mid+1

print(answer)