#   What is the 10 001st prime number?


def prime_factors(n):

    if n < 2:
        return 'Number must be greater than 1'
    elif type(n) is not int:
        return 'Number must be Integer!'
    else:
        l = list(range(1000000))
        l[1] = 0
        sum = 0
        for i in l:
            if i > 0:
                sum += 1
                if sum == n:
                    return i
                for j in range(i + i, len(l), i):
                    l[j] = 0