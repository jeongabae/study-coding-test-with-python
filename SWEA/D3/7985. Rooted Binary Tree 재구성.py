def solve_tree_levels(K, inorder):
    levels = []
    num_nodes = len(inorder)

    # 레벨 0부터 K-1까지 각 레벨의 노드를 순서대로 추출
    for depth in range(K):
        # 각 레벨의 노드의 간격 계산
        step = 2 ** (K - depth - 1)
        # 현재 레벨의 시작 위치는 첫 노드에서 중간값으로 이동해 계산
        start = step - 1

        # 해당 레벨의 노드들을 추출하여 리스트에 추가
        level_nodes = [inorder[i] for i in range(start, num_nodes, step * 2)]
        levels.append(" ".join(map(str, level_nodes)))

    return levels


# 입력 처리 및 결과 출력
T = int(input())
for t in range(1, T + 1):
    K = int(input())
    inorder = list(map(int, input().split()))
    result = solve_tree_levels(K, inorder)
    print(f"#{t}", end=' ')
    for line in result:
        print(line)