def house_robber(money:list[int]) -> int:
    wout_first_house = _house_robber(money, 1, len(money))
    wout_last_house = _house_robber(money, 0, len(money)-1)
    return max(wout_first_house, wout_last_house)   

def _house_robber(money:list[int], start:int, end:int) -> int:
    if start >= end:
        return 0
    
    include_first_amount = money[start] + _house_robber(money, start+2, end)
    exclude_first_amount = _house_robber(money, start+1, end)

    return max(include_first_amount, exclude_first_amount)