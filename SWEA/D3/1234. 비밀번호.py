# for test_case in range(1, 11):
#     n, arr = input().split()
#     arr = list(arr)
#     i = 0
#     while True:
#         if i==len(arr)-1:
#             break
#         if arr[i] == arr[i+1]:
#             del arr[i:i+2]
#             i = i-1
#             continue
#         i+=1
#     print(f'#{test_case}', ''.join(arr))

#스택 이용 풀이
for test_case in range(1, 11):
    n, arr = input().split()
    stack = []

    for char in arr:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    print(f'#{test_case}', ''.join(stack))