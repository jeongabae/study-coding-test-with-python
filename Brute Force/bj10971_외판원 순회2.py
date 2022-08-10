import sys

N = int(input()) #도시의 개수
W = [list(map(int, input().split())) for _ in range(N)] #비용 행렬
visited = [] #방문 도시 list
min_cost = sys.maxsize #int의 최대값이 sys.maxsize이므로 이렇게 일단 해둠.

def dfs(start, curr, cost): #출발하는도시(여기로 돌아와야함), 현재 방문 도시 ,비용
    global min_cost

    if len(visited) == N: #N개의 모든 도시를 방문했다면
        if W[curr][start] != 0: # 마지막으로 방문한 도시에서 처음 출발한 도시로 가는 비용이 0이 아니라면
            # (경우에 따라서 도시 i에서 도시 j로 갈 수 없는 경우도 있으며 이럴 경우 W[i][next]=0가 있기때문에) curr도시에서 처음 출발한 도시로 갈 수 있는지 체크해야함.
            min_cost = min(min_cost, cost + W[curr][start]) # 갈 수 있다면 그 전에 구한 최소 비용 값과 비교해서 작으면 대입
            print(visited,min_cost)
            return

    for next in range(N): #도시의 개수 만큼 반복문을 돈다.
        #현재 도시에서 next도시로 갈 수 있는 도시의 비용이 0이 아니고(갈 수 있고), 이미 방문한 도시가 아니고, 이동 비용이 저장되어있는 최소값 보다 작다면
        if W[curr][next] != 0 and next not in visited and cost < min_cost:
            visited.append(next) #next도시를 방문목록에 추가
            print(visited)
            dfs(start, next, cost + W[curr][next]) #next도시 방문
            visited.pop() #도시 방문 완료 시 방문 visited에서 꺼냄

#어느 도시에서 시작하여 돌아올 건지.
for i in range(N):
    visited.append(i) #i번째 도시 방문.
    dfs(i, i, 0) #시작을 i도시로 하면서 처음으로 i방문. 자기에서 자기로 가는 방문 비용은 0이니까 처음 cost는 0
    visited.pop() #i에서 i번째로 가는 최소값 구했으니까 i pop

print(min_cost)