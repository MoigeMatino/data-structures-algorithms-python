def house_robber(money:list[int]) -> int:
    memo1 = {}
    memo2 = {}
    wout_first_house = _house_robber(money, 1, len(money), memo1)
    wout_last_house = _house_robber(money, 0, len(money)-1, memo2)
    return max(wout_first_house, wout_last_house)

def _house_robber(money:list[int], start:int, end:int, memo:dict[int,int]) -> int:
    if start in memo:
        return memo[start]
    
    if start >= end:
        return 0
    
    include_first_amount = money[start] + _house_robber(money, start+2, end, memo)
    exclude_first_amount = _house_robber(money, start+1, end, memo)

    memo[start] = max(include_first_amount, exclude_first_amount)
    return memo[start]