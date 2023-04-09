def solution(polynomial):
    p = polynomial.split(' + ')
    x, c = 0, 0

    for i in p:
        if i[-1] == 'x':
            x += 1 if i[0] == 'x' and len(i) == 1 else int(i[:-1])
        else:
            c += int(i)

    a = str(x) + 'x' if x else ''
    if x == 1: a = 'x'
    b = str(c) if c else '0'
    plus = ' + ' if a and b else ''

    if x > 0 and c > 0:
        return a + plus + b
    else:
        return a if a else b