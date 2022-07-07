import sys

sieve = [False, False] + [True] * (1000000-1)

#에라토스테네스의 체 이용
for i in range(2, 1001): #n(1000000)의 최대 약수가 sqrt(n) 이하이므로 여기까지만(1000) 검사!
    if sieve[i]:
        for j in range(2*i, 1000001, i):
            sieve[j] = False

while True:
    n = int(sys.stdin.readline().rstrip())
    if n == 0: break

    for i in range(3, len(sieve)):
        if sieve[i] and sieve[n-i]:
            print(n, "=", i, "+", n-i)
            break