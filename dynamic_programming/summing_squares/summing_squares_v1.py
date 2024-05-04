from math import sqrt, floor
def summing_squares(target: int) -> int:
    if target == 0:
        return 0
    
    min_squares = float('inf')
    
    for num in range(1, floor(sqrt(target) + 1)):
        num_square = num * num
        remainder = target - num_square
        no_of_squares = 1 + summing_squares(remainder)
        if no_of_squares < min_squares:
            min_squares = no_of_squares
    
    return min_squares
