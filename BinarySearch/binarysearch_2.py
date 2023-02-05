array=[1,2,3,4,5]
start=0
end=len(array)-1

def binary(X,):
    mid = (start+end)//2
    if array[mid] == X:
        return mid
    else:
        if array[mid]>X:
            binary
