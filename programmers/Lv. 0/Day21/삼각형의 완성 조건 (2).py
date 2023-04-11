def solution(sides):
    s = sum(sides)
    ma = max(sides)
    mi = min(sides)
    return sum(1 for i in range(1,s+1) if (i>=ma and i<s) or (ma>i and ma<mi+i))

"""
기존에 알고 있는 변이 a, b라고 하자.(a>b)
이때, 새로 입력 받는 c가 a보다 클 수도 있고 같을 수도 있고 작을 수도 있다.
i) if c> a,  c > a > b가 된다.
a + b > c  ->  a + b > c > a가 된다.
가능한 c의 갯수는 b - 1개

ii) if c<a, a > b, a > c 가 된다.
b + c > a -> b + c > a > c가 된다.
가능한 c의 갯수는 b - 1개

iii) if c=a
 가능한 c의 개수는 c = a 1개.

i)~iii) 다 합하면 (b - 1) + (b - 1) + 1 = 2 * b - 1 개가 된다.
(이때 초기 조건에 따라 b는 a보다 작음)

def solution(sides):
    return 2 * min(sides) - 1

"""