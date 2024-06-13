#!/usr/bin/python3
'''Minimum Operations'''

def minOperations(n):
    '''
    alculates the fewest number of operations needed to
    result in exactly n H characters
    '''
    if n <= 1:  # If n is impossible to achieve
        return 0
    num_operations = 0  # number of operations required
    i = 2  # initialize i to the smallest prime factor
    # Divide n by its prime factors, starting with the smallest prime factor
    while i <= n:
        if n % i == 0:
            n //= i
            num_operations += i
            i = 2  # reset the value of i
        else:
            i += 1
    return num_operations
