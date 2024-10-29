a, b = map(int, input().split())
print('A' if (a == 1 and b == 3) or (a == 2 and b == 1) or (a == 3 and b == 2) else 'B')

# 이런 풀이도 있다(시간 살짝 더 오래걸림)(메모리는 더 작게 잡아먹음)
# a, b = map(int, input().split())
# a_win = [0, 3, 1, 2]
# print('A' if a_win[a] == b else 'B')
