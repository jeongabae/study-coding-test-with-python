# 백준 2529번 : 부등호 : 브루트포스, 백트래킹
import sys
def input():
    return sys.stdin.readline().rstrip()

k = int(input())
arr = input().split() # 부등호 입력받음
check = [0]*10 #0~9 숫자를 사용했으면 1 사용 안했으면 0
ans=[] # 부등호 만족하는 숫자면 넣음 (오름차순으로 여기에 들어감)

def ok(x,y,op): # 부등호 만족시키는지 확인하는 함수
    if op=='<' and x>y: # 부등호가 < 일때는 x<y가 되어야하는데 x>y이면 부등호 맞지않는 것.
        return False
    if op=='>' and x<y:  # 부등호가 > 일때는 x>y가 되어야하는데 x<y이면 부등호 맞지않는 것.
        return False
    return True # 그 외는 부등호가 다 맞다고 볼 수 있음

def dfs(idx, num):
    if idx==k+1: #숫자가 k+1개가 되면 필요한 숫자만큼 온거니까.(부등호가 k개니까 숫자 k+1 필요)
        ans.append(num) #answer 배열에 지금까지 쌓아온 숫자 추가
        return

    for i in range(10):
        if check[i]: continue #이미 사용한 숫자면 사용 불가
        if idx==0 or ok(num[idx-1],str(i),arr[idx-1]): # 처음 숫자는 아무거나 와도 되니까 idx==0인 경우 혹은 처음 숫자가 아니라면 부등호를 만족하는 숫자면 해당 숫자 추가(사용)
            check[i] = 1 #i를 사용
            dfs(idx+1, num+str(i)) # 그 다음 인덱스 숫자 고르기 위해 idx+1, 그리고 i를 숫자문자열에 추가.
            check[i] = 0

dfs(0,'') #처음엔 인덱스 0부터 시작
ans.sort()
print(ans[-1]) #ans 맨 뒤에 있는 숫자가 가장 큼
print(ans[0])  #ans 맨 앞에 있는 숫자가 가장 작음