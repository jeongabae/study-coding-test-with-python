T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    b = bin(m)[2:]

    ans= b[-n:]

    if ans == "1"*n:
        print(f"#{test_case} {'ON'}")
    else:
        print(f"#{test_case} {'OFF'}")

