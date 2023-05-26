def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n - 1) + fib(n - 2)

"""
Time: O(2^n)
Space: O(n)

"""