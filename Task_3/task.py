#   What is the largest prime factor of the number 600851475143 ?


def prime_factors(n):
    if n < 2:
        return 'Number must be greater than 1'
    elif type(n) is not int:
        return 'Number must be Integer!'
    else:
        my_list = []
        for no3 in range(2, n):
            i = 0
            if n % no3 == 0:
                for a in range(1, int(no3)):
                    if no3 % a == 0:
                        i = i + 1
                if i == 1:
                    my_list.append(no3)
        return max(my_list)