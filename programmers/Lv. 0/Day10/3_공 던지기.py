def solution(numbers, k):
    return numbers[2*(k-1) % len(numbers)]
"""
1) 2칸씩 이동하므로 2를 곱함
2) 0번 인덱스부터 시작해서 '공을 던지는 사람'을 찾아야 하므로 (k-1) (공을 받는 사람으로 문제가 바뀌면 2*k 해주면 됨.)
3) numbers 길이를 넘어갈 수 없으므로 % 나머지 연산 사용
"""