import sys
def input():
    return sys.stdin.readline().rstrip()

N = int(input())
M = int(input())
broken = []
if M: #고장난 버튼이 있는 경우에는 셋째 줄에는 고장난 버튼이 주어짐
    broken = list(map(int, input().split()))
"""
#if N==100: #이거 안 넣는게 시간 더 빠름.
#    print(0)
#    exit()
"""
min_cnt = abs(100 - N) # 현재 보고있는 채널에서 + or -만 사용하여 이동하는 경우. 처음에는 현재 채널이 100이므로 abs(100-N)으로 초기화.

for num in range(1000001): #채널 N의 범위는 0 ≤ N ≤ 500,000이지만 갈 수 있는 채널은 무한하다.
                            # 만약, 500,000이 입력으로 들어오고 0,1,2,3,4,5가 고장난 경우 600,000에서 -를 사용하는게 min_cnt가 되기 때문에 범위를 500,000*2로.
    num = str(num)

    for j in range(len(num)):
        # num의 각 자리수가 고장났는지 check -> 고장 났으면 break
        if int(num[j]) in broken:
            #print("num",num,"num[j]",num[j],min_cnt)
            break

        # 0~1000001 숫자 중 하나인 num의 각 자리수가 고장난 숫자 없이 마지막 자리까지 왔다면 min_count 비교 후 업데이트
        elif j == len(num) - 1:
            min_cnt = min(min_cnt, abs(int(num) - N) + len(num))
            #print("마지막고장X", num, min_cnt)
            break
print(min_cnt)
"""다른 분 코드 125612KB	276ms	PyPy3
target=int(input())
N=int(input())

ans=abs(100-target)
if N:
    broken=set(input().split())
else:
    broken=set()

for i in range(1000001):
    for j in str(i):
        if j in broken:
            break
    else:
        ans=min(ans,len(str(i))+abs(target-i))
print(ans)
"""