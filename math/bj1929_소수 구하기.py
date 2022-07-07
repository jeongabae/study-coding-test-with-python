#좋은 방법 : 에라토스테네스의 체
#아래는 에라토스테네스의 체 이용한 풀이이다!
m,n = map(int,input().split())
sieve = [False, False] + [True] * (n-1) #0과 1은 소수가 아님 #2부터는 일단 True라고 해놓고 for문에서 나머지 해결!
primes=[]

sqrt_n = int(n**0.5) #n의 최대 약수가 sqrt(n) 이하이므로 여기까지만 검사!
for i in range(2,sqrt_n+1):
    if sieve[i]:
        for j in range(2*i,n+1,i): #지워지지 않은 수 중 제일 작은 2를 소수로 채택하고, 나머지 2의 배수를 모두 지운다.(false로...)
            sieve[j] = False
for i in range(2,n+1):#이게 i가 2부터 시작하니까 만약에 3~16사이의 소수를 찾아라면, 2가 안들어가야 하므로..이런..것!
    if sieve[i] and i >= m:
        primes.append(i)
for i in primes:
    print(i)
""" 에라토스테네스 체 이용 기본 풀이
m,n = map(int,input().split())
sieve = [False, False] + [True] * (n-1) #0과 1은 소수가 아님 #2부터는 일단 True라고 해놓고 for문에서 나머지 해결!
primes=[]
for i in range(2,n+1):
    if sieve[i]:
        for j in range(2*i,n+1,i): #지워지지 않은 수 중 제일 작은 2를 소수로 채택하고, 나머지 2의 배수를 모두 지운다.(false로...)
            sieve[j] = False
        if i >= m: #이게 i가 2부터 시작하니까 만약에 3~16사이의 소수를 찾아라면, 2가 안들어가야 하므로..이런..것!
            primes.append(i)
for i in primes:
    print(i)
"""

"""시간초과
M, N = map(int,input().split())
n = []
for i in range(M,N+1):
    is_ok = 1
    if i != 1:
        for j in range(2, i):
            if i % j == 0:
                is_ok = 0
                break
        if is_ok:
            n.append(i)
for k in n:
    print(k)
"""
"""맞긴 하는데 시간 오래 걸림 
M, N = map(int,input().split())
n = []
for i in range(M,N+1):
    if i == 1:
        continue
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            break
    else:
        print(i)
"""
"""
모든 수를 돌면서 나누어 떨어지는 수가 있는지 없는지 보면 된다!
근데, 꼭 모든 수를 봐야하는건 아니다. 해당 수의 제곱근까지만 나눠보면 됨!
약수는 대칭으로 이루어져있기 때문에
(예) 12의 약수는 1 2 3 4 6 12 / 1*12 , 2*6, 3*4 로 대칭
25의 약수는 1 5 25 / 1*25 , 5*5 로 대칭
제곱근 보다 같거나 작은 수까지만 나눠보고 나누어 떨어지는게 있냐 없냐 확인하면 된다
"""
