def sum_possible(amount, numbers):
    if amount == 0:
        return True
    
    if amount < 0:
        return False

    for num in numbers:
        if sum_possible(amount-num, numbers):
            return True
        
    return False

"""
brute force

a - amount
n - length of numbers list

Time: O(n^a)
Space: O(n)

"""