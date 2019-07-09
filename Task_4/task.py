#   Find the largest palindrome made from the product of two 3-digit numbers.


def palindrome(n):
    if n < 2:
        return 'Number must be greater 1'
    elif type(n) is not int:
        return 'Number must be Integer!'
    else:
        a = pow(10, n) - 1
        b = pow(10, n-1) - 1
        for i in range(a, b, -1):
            for j in range(a, b, -1):
                m = i * j
                if str(m) == str(m)[::-1]:
                    return str(i*j)