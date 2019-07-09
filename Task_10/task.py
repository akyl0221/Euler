#   Find the sum of all the primes below two million.


def summ_primes(n):
    if n < 2:
        return 'Number must be greater 2'
    elif type(n) is not int:
        return 'Number must be Integer!'
    else:
        l = list(range(n))
        l[1] = 0
        sum = 0
        for i in l:
            if i > 0:
                sum += i
                for j in range(i+i, len(l), i):
                    l[j] = 0
        return sum