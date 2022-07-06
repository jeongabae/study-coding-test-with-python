import sys

N = sys.stdin.readline().rstrip()
st = []
ans = 0

for i in range(len(N)):
    if N[i]=='(':
        st.append(i)
    else:
        ans+= len(st)-1 if i-st[-1]==1 else 1
        st.pop()
print(ans)

"""1등분 코드
import sys

def solution(arrangement):
    arrangement = arrangement.replace('()', '0');
    temp = 0    # "("의 개수 = 현재 진행중인 막대기 개수
    answer = 0

    for i in arrangement:
        if i == "(": temp += 1
        elif i == "0": answer += temp
        else:
            temp -= 1
            answer += 1
    return answer

x = sys.stdin.readline().rstrip()
print(solution(x))
"""