def counting_change(amount: int, coins:list[int]) -> int:
    return _counting_change(amount, coins, 0)

def _counting_change(amount: int, coins: list[int], idx: int) -> int:
    if amount == 0:
        return 1
    
    if amount < 1:
        return 0
    
    coin = coins[idx]

    total_ways = 0
    
    for qty in range(amount//coin +1):
        remainder_amount = amount - (qty*coin)
        ways_for_remainder = _counting_change(amount, remainder_amount, idx+1)
        total_ways += ways_for_remainder

    return total_ways
        
        