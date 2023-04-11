def solution(numbers):
    n = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for idx, num in enumerate(n):
        numbers = numbers.replace(num, str(idx))
    return int(numbers)


"""
def solution(numbers):
    for num, eng in enumerate(["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
        numbers = numbers.replace(eng, str(num))
    return int(numbers)
"""