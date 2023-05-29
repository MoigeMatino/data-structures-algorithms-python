def sum_possible(amount, numbers):
    return _sum_possible(amount, numbers, {})

def _sum_possible(amount, numbers, memo):
    if amount in memo:
        return memo[amount]
    
    if amount == 0:
        return True
    
    if amount < 0:
        return False

    for num in numbers:
        if _sum_possible(amount-num, numbers, memo):
            memo[amount] = True
            return True
    
    memo[amount] = False
        
    return False

"""
memoization

a = amount
n = length of numbers
Time: O(a*n)
Space: O(a)

"""