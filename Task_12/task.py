import time


def num_divisors(n):
    if n % 2 == 0: n = n / 2
    divisors = 1
    count = 0
    while n % 2 == 0:
        count += 1
        n = n / 2
    divisors = divisors * (count + 1)
    p = 3
    while n != 1:
        count = 0
        while n % p == 0:
            count += 1
            n = n / p
        divisors = divisors * (count + 1)
        p += 2
    return divisors


def find_triangular_index(factor_limit):
    n = 1
    lnum, rnum = num_divisors(n), num_divisors(n + 1)
    while lnum * rnum < factor_limit:
        n += 1
        lnum, rnum = rnum, num_divisors(n + 1)
    return n


def find_triangle(n):
    if n < 1:
        return 'Number must be greater 1'
    elif type(n) is not int:
        return 'Number must be Integer!'
    else:
        index = find_triangular_index(n)
        triangle = (index * (index + 1)) / 2
        return triangle
