T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    arr = list(input().split())
    mid = n//2+1 if n%2!=0 else n//2
    d1 = arr[:mid]
    d2 = arr[mid:]
    ans = []
    for i in range(n):
        if i%2==0:
            ans.append(d1.pop(0))
        else:
            ans.append(d2.pop(0))

    print(f'#{test_case}', *ans)