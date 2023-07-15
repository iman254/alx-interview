#!/usr/bin/python3
"""A method that calculates the fewest number of operations
needed to result in exactly n H characters in the file. """


def minOperations(n):
    """fewest number of operations needed to return n H characters"""
    if n <= 1:
        return 0
    operation = 0
    factors = 2

    while factors * factors <= n:
        if n % factors == 0:
            operation += factors
            n //= factors
        else:
            factors += 1

    if n > 1:
        operation += n

    return operation
