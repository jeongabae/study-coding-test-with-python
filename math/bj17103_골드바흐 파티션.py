import sys

T = int(sys.stdin.readline().rstrip())
n = [int(sys.stdin.readline().rstrip()) for _ in range(T)]
m = max(n)
sieve = [False, False] + [True] * (m - 1)
# 에라토스테네스의 체 이용
for i in range(2, int(m ** 0.5) + 1):  # m의 최대 약수가 sqrt(m) 이하이므로 여기까지만 검사!
    if sieve[i]:
        for j in range(2 * i, m + 1, i):
            sieve[j] = False
for i in n:
    cnt = 0
    for j in range(i // 2 + 1):
        if sieve[j] and sieve[i - j]:
            # print(n, "=", i, "+", n-i)
            cnt += 1
    print(cnt)
"""
이 문제 주의!!! 맞는거같은데 틀렸습니다 판정받은 이유 ㅠㅠ...
골드바흐의 추측 정의와 이 문제에서 사용한 골드바흐의 추측 정의가 다름!!

문제에서 주어진 정의를 사용해야 맞았습니다를 받을 수 있음!

4 = 2 + 2 이므로 입력이 4일 때의 출력은 1 이 되어야 함!
(ps. 4 이외의 입력에서는 2 를 포함한 파티션이 없음.)

그래서 for j in range(i//2+1):로 범위 수정했더니 바로 맞음..ㅋ
원래 골드 바흐의 정의로는 for j in range(3, i//2+1):이 되어야하지만
이 문제에서는 2를 포함해야했던 것...
"""