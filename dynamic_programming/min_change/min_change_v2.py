def min_change(amount, coins):
    ans = _min_change(amount, coins, {})
    if ans == float('inf'):
        return -1
    else:
        return ans

def _min_change(amount, coins, memo):
    if amount in memo:
        return memo[amount]
    
    if amount == 0:
        return 0
    
    if amount < 0:
        return float('inf')
    
    min_coins = float('inf')
    for coin in coins:
        num_coins = 1 + _min_change(amount - coin, coins, memo)
        min_coins = min(min_coins, num_coins)
        
    memo[amount] = min_coins
    return min_coins

"""
memoization

a = amount
c = # coins
Time: O(a*c)
Space: O(a)

"""