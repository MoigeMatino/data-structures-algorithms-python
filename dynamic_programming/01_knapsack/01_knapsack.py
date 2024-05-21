def find_max_knapsack_profit(capacity:int, weights:list[int], values:list[int]) -> int:
    memo = {}
    return _find_max_knapsack_profit(capacity, weights, values, 0, memo)

def _find_max_knapsack_profit(capacity:int, weights:list[int], values:list[int], idx:int, memo:dict):
    key = idx, capacity
    if key in memo:
        return memo[key]
    
    if capacity == 0 or idx == len(weights):
        return 0
    
    current_weight = weights[idx]
    if current_weight <= capacity:
        include_current = values[idx] + _find_max_knapsack_profit(capacity-current_weight, weights, values, idx+1, memo)
        exclude_current = _find_max_knapsack_profit(capacity, weights, values, idx+1, memo)
        memo[key] = max(include_current, exclude_current)
        return memo[key]
    else:
        memo[key] = _find_max_knapsack_profit(capacity, weights, values, idx+1, memo)
        return memo[key]
    