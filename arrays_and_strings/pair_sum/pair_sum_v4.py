def pair_sum(numbers, target_num):
    tracker_list = {}
    for idx, num in enumerate(numbers):
        if (diff:=target_num-num) in tracker_list:
            return tracker_list[diff],idx
        tracker_list[num] = idx
    return None

