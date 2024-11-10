T = int(input())
for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    div = n//10
    grades = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    student = []
    for _ in range(n):
        t1, t2, hw = map(int, input().split())
        student.append((t1*35+t2*45+hw*20)/100)
    sorted_st = sorted(student, reverse=True)
    k_score = student[k-1]
    k_rank = sorted_st.index(k_score)
    print(f'#{test_case} {grades[k_rank//div]}')