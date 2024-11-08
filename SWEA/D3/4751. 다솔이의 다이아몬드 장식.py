T = int(input())
for test_case in range(1, T+1):
    word = input()
    length = len(word)
    line1 = '..#.'
    line2 = '.#'
    line3 = '#.'
    print(line1 * length + '.')
    print(line2 * length * 2 + '.')
    for i in range(length):
        print(line3 + word[i] + '.', end='')
    print('#')
    print(line2 * length * 2 + '.')
    print(line1 * length + '.')