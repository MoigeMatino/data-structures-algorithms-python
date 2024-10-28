def happy_number(n: int) -> bool:
    slow = n
    fast = squared_digits_sum(n)
    
    while fast != slow or n != 1:
        slow = squared_digits_sum(slow)
        fast = squared_digits_sum(squared_digits_sum(fast))
        
    if fast == slow:
        return False
    return True
    
def squared_digits_sum(n: int) -> int:
    digits_sum = 0
    while n > 0:
        n, digit = divmod(n,10)
        digits_squared = digit * digit
        digits_sum += digits_squared
    return digits_sum