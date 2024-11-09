T = int(input())  # 테스트 케이스의 수 입력
for test_case in range(1, T + 1):
    n = int(input())  # 표현하고자 하는 자연수 N 입력
    cnt = 0  # N을 연속된 자연수의 합으로 표현할 수 있는 경우의 수

    for i in range(1, n + 1):  # 시작 자연수 i
        sum_val = 0  # 연속된 자연수의 합 초기화
        for j in range(i, n + 1):  # 시작점부터 연속해서 더해가는 자연수 j
            sum_val += j
            if sum_val == n:  # 합이 N과 같다면 경우의 수 증가
                cnt += 1
                break  # 다음 시작 숫자로 넘어가기
            elif sum_val > n:  # 합이 N보다 크다면 이 경우는 불가능
                break

    print(f"#{test_case} {cnt}")  # 결과 출력