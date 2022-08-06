import sys
N, M = map(int, sys.stdin.readline().split())
used = [0] * (N + 1)
ans = []

def dfs(idx,start): #idx는 몇 번째에 있느냐를 의미 만약에 1 2 3이라는 수열이면 1은 idx=0자리 2는 idx=1, 3는 idx=3
    if idx==M:#만약 길이가 M=3인 수열을 만드는데 idx가 3이면 0,1,2 세 개의 숫자가 찼다는거니까 수열 출력
        print(' '.join(ans))
        return

    for i in range(start, N+1):#길이가 M이 아니라면 start부터 N까지의 숫자를 확인
        if not used[i]: #중복 없어야 하므로.. 만약에 수열에 숫자i가 아직 없다면
            used[i] = 1 #방문(사용) 처리를해주고,
            ans.append(str(i)) #그 숫자를 수열에 넣는다.
            dfs(idx + 1,i+1) #그리고 그 다음 수가 뭐가 올 수 있을지 찾는다.(가지치기) start는 지금까지 수열에 있는 수보다 커야하므로 1더해준다.
            used[i] = 0 #어떤 수열을 찾았으므로 다음 수열을 찾기 위해 수 하나를 꺼내준다. 즉, 방문(사용)하지 않았다고 표시.
            ans.pop() # 수열에서 수를 꺼냄
dfs(0,1) #0번째 수부터 시작수는 1부터 길이가 M인 수열을 만들자.
