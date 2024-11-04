T = int(input())
for test_case in range(1, T + 1):
    a, b = map(int, input().split())
    cnt = 0
    for i in range(a, b+1):
        st_i = str(i)
        if st_i == st_i[::-1]:
            root = int(i**0.5)
            if root*root == i:
                root = str(root)
                if root == root[::-1]:
                    cnt+=1
    print(f'#{test_case} {cnt}')