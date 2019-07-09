# Find the sum of all the multiples of 3 or 5 below 1000.
def summ_calculate():
    sum = 0
    i = 0
    while i < 1000:
        sum += i
        i += 3
    i = 0
    while i < 1000:
        if (i % 3) != 0:
            sum += i
        i += 5
    return sum

print("Sum is: %d" % summ_calculate())
if __name__ == '__main__':
    summ_calculate()
