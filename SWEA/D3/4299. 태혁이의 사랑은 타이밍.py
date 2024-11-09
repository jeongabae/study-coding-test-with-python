T = int(input())
for test_case in range(1, T+1):
    a = input()
    cnt = 0
    for i in range(len(a)):
        if ord(a[i])-97==cnt:
            cnt+=1
        else:
            break
    print(f'#{test_case} {cnt}')