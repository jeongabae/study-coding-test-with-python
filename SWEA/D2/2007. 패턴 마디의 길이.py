T = int(input())
for test_case in range(1, T + 1):
    string = input()
    for length in range(1, 11):
        pattern = string[:length]
        if pattern * (30 // length) == string[:length * (30 // length)]:
            print(f'#{test_case} {length}')
            break