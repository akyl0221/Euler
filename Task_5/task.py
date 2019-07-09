#   What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


def ifDividesAll(num):
    for i in range(2, num+1):
        if num % i != 0:
            return False
    return True


def smallest_positive(n):
    if n < 10:
        return 'Number must be greater 9'
    elif type(n) is not int:
        return 'Number must be Integer!'
    else:
        while True:
            if ifDividesAll(n):
                break
            else:
                n = n + 1
    return (n)