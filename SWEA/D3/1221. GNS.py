# 풀이1
# import sys
# sys.stdin = open("GNS_test_input.txt", "r")
# T = int(input())
# dic = {"ZRO":0, "ONE":1, "TWO":2, "THR":3, "FOR":4, "FIV":5, "SIX":6, "SVN":7, "EGT":8, "NIN":9}
# reversed_dic = {v: k for k, v in dic.items()}
# for test_case in range(1, T+1):
#     _, n = input().split()
#     n = int(n)
#     arr = list(input().split())
#     arr_n = []
#     for i in arr:
#         arr_n.append(dic[i])
#     arr_n.sort()
#     for i in range(n):
#         arr[i] = reversed_dic[arr_n[i]]
#     print(f'#{test_case}')
#     print(*arr)

# 풀이2
import sys
sys.stdin = open("GNS_test_input.txt", "r")
T = int(input())
for test_case in range(1, T+1):
    _, n = input().split()
    n = int(n)
    arr = list(input().split())
    dic = {"ZRO": 0, "ONE": 0, "TWO": 0, "THR": 0, "FOR": 0, "FIV": 0, "SIX": 0, "SVN": 0, "EGT": 0, "NIN": 0}
    for i in arr:
        dic[i]+=1
    print(f'#{test_case}')
    for i in dic:
        for _ in range(dic[i]):
            print(i, end=' ')
    print()
