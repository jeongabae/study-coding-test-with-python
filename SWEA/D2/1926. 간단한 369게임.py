# n = input()
# for i in range(1, int(n)+1):
#     clap = False
#     for j in str(i):
#         if j in ('3', '6', '9'):
#             print('-', end='')
#             clap = True
#     if not clap:
#         print(i, end='')
#     print('', end=' ')
n = input()
for i in range(1, int(n)+1):
    if '3' in str(i) or '6' in str(i) or '9' in str(i):
        cnt = str(i).count('3') + str(i).count('6') + str(i).count('9')
        print('-' * cnt, end=' ')
    else:
        print(i, end=' ')