import sys
sys.stdin = open("test_input_1213.txt", "r")
for test_case in range(1, 11):
    t = int(input())
    search = input()
    s = input()
    cnt = s.count(search)
    print(f'#{test_case} {cnt}')