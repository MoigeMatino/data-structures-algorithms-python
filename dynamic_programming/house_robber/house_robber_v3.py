def house_robber(money:list[int]) -> int:
    if len(money) == 0:
        return 0
    
    if len(money) == 1:
        return money[0]
    
    wout_first_house = _house_robber(money[1:])
    wout_last_house = _house_robber(money[:-1])
    return max(wout_first_house, wout_last_house)

def _house_robber(money:list[int]) -> int:
    table = [0 for i in range(len(money)+1)]
    table[0] = 0
    table[1] = money[0]
    for x in range(2, len(money)+1):
        # ? why do we do money[x-1] here, why not money[x]
        including_current_amount = money[x-1] + table[x-2]
        excluding_current_amount = table[x-1]
        table[x] = max(including_current_amount, excluding_current_amount)

    return table[-1]