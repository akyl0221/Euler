#  Find the difference between the sum of the squares of the first
#  one hundred natural numbers and the square of the sum.


def difference_sqare_summ(n):
    if n < 2:
        return 'Number must be greater 1'
    elif type(n) is not int:
        return 'Number must be Integer!'
    else:
        num2 = sum([i * i for i in range(1, n + 1)])
        num = sum(range(1, n + 1))
        num = num * num
        return num - num2
