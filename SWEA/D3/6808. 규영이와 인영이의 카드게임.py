# T = int(input())
# for test_case in range(1, T+1):
#     card = list(map(int, input().split()))
#     card2 = []
#     for i in range(1, 19):
#         if i not in card:
#             card2.append(i)
#
#     print(f'#{test_case} {x} {y}')

ALL_CARDS = set(range(1, 19))  # 1부터 18까지의 카드
def backtrack(round, gyu_score, in_score, gyu_cards, in_cards, win_count, lose_count):
    if round == 9:  # 9라운드가 끝났을 때
        if gyu_score > in_score:
            win_count[0] += 1
        elif gyu_score < in_score:
            lose_count[0] += 1
        return

    gyu_card = gyu_cards[round]  # 규영이가 사용하는 카드
    # 인영이의 카드 중 사용되지 않은 카드 고르기
    for i in range(9):
        if not used[i]:  # 아직 사용되지 않은 카드
            used[i] = True  # 카드 사용 표시
            in_card = in_cards[i]  # 인영이가 사용할 카드

            # 규영이 카드가 인영이 카드보다 크면 규영이가 이긴다
            if gyu_card > in_card:
                backtrack(round + 1, gyu_score + gyu_card + in_card, in_score, gyu_cards, in_cards, win_count, lose_count)
            else:
                backtrack(round + 1, gyu_score, in_score + gyu_card + in_card, gyu_cards, in_cards, win_count, lose_count)

            used[i] = False  # 카드 사용 취소

T = int(input())  # 테스트 케이스 수
for test_case in range(1, T + 1):
    gyu_cards = list(map(int, input().split()))  # 규영이가 받은 카드
    in_cards = list(ALL_CARDS - set(gyu_cards))  # 인영이가 받은 카드
    win_count = [0]  # 승리 횟수
    lose_count = [0]  # 패배 횟수
    used = [False] * 9  # 사용된 카드 추적 배열
    backtrack(0, 0, 0, gyu_cards, in_cards, win_count, lose_count)  # 백트래킹 시작
    print(f"#{test_case} {win_count[0]} {lose_count[0]}")

# from itertools import permutations
# ALL_CARDS = set(range(1, 19))  # 1부터 18까지의 카드
# T = int(input())  # 테스트 케이스 수
# for test_case in range(1, T + 1):
#     gyu_cards = list(map(int, input().split()))  # 규영이가 받은 카드
#     in_cards = list(ALL_CARDS - set(gyu_cards))  # 인영이가 받은 카드
#     g_win = 0
#     i_win = 0
#     for i in list(permutations(in_cards, 9)):
#         g_sum = 0
#         i_sum = 0
#         for j in range(9):
#             gy = gyu_cards[j]
#             iy = i[j]
#             if gy>iy:
#                 g_sum+=gy+iy
#             else:
#                 i_sum+=gy+iy
#     if g_sum>i_sum:
#         g_win+=1
#     else:
#         i_win+=1
#     print(f"#{test_case} {g_win} {i_win}")