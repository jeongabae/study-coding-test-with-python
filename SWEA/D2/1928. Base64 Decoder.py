# 1. 표 보고 입력받은 문자들 -> 각각 대응하는 숫자로 변경
# 2. 각 숫자들을 6자리 이진수로 표현 -> 이 이진수들을 한 줄로 쭉 이어 붙임.
# 3. 한 줄로 쭉 이어붙인 이진수들을 8자리씩 끊어서 십진₩ 수로 바꾼걸 아스키 코드로 변환

T = int(input())
table = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
         'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
         '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '/']
for test_case in range(1, T+1):
    a = input()
    zinsu = ''

    for s in a:
        b = bin(table.index(s))[2:]
        zinsu+=b.zfill(6)

    result = []
    for i in range(0, len(zinsu), 8):
        result.append(chr(int(zinsu[i:i+8], 2)))
    print("#"+str(test_case), ''.join(result))