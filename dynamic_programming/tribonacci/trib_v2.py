def tribonacci(n):
    memo = {}
    return _tribonacci(n, memo)

def _tribonacci(n, memo):
    if n in memo:
        return memo[n]
        
    if n == 0 or n == 1:
        return 0
    
    if n == 2:
        return 1
    
    memo[n] = _tribonacci(n-1, memo) + _tribonacci(n-2, memo) + _tribonacci(n-3, memo)
    
    return memo[n]

"""
memoized solution

Time: O(n)
Space: O(n)

"""