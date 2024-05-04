def min_change(amount:int, coins:list[int]) -> int:
    ans = _min_change(amount, coins)
    if ans == float('inf'):
        return -1
    return ans

def _min_change(amount:int, coins:list[int]) -> int:
    if amount == 0:
        return 0
    
    if amount < 0:
        return float('inf')
    min_coins = float('inf')
    for coin in coins:
        remaining_amount = amount - coin
        num_of_coins = 1 + _min_change(remaining_amount, coins)
        if num_of_coins < min_coins:
            min_coins = num_of_coins
            
    return min_coins
