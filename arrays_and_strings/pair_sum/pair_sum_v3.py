def pair_sum(numbers, target_sum):
    tracker = {}
    for index,num in enumerate(numbers):
        diff = target_sum-num
        if num not in tracker:
            tracker[num] = index
        if diff in tracker and tracker[diff] != index:
            result=tracker[diff],index
    
    return result 