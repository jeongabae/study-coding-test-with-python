T = int(input())
for test_case in range(1, T + 1):
    n, a, b = map(int, input().split())
    s = a+b
    min_ab = min(a, b)
    all_min, all_max = 0, min_ab
    all_min = 0 if n>=s else s-n
    print(f'#{test_case} {all_max} {all_min}')