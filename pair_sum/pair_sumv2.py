def pair_sum(numbers, target_sum):
    for index,num in enumerate(numbers):
        diff=target_sum-num
        if diff in numbers and diff != num:
            result=index, numbers.index(diff)    
        
    return result