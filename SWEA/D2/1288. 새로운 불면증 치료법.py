def mark_digits(num, nums):
    for i in str(num):
        nums[int(i)] = 1

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    cnt = 1
    nums = [0]*10
    mark_digits(n, nums)

    while True:
        cnt += 1
        a = n*cnt
        mark_digits(a, nums)

        if sum(nums) == 10:
            print(f'#{test_case} {a}')
            break