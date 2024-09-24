def circular_array_loop(nums: list) -> bool:
    size = len(nums)
    
    # Iterate over each index in the array
    for index in range(size):
        slow = fast = index
        forward = nums[index] > 0
        
        while True:
            slow = next_step(slow, nums[slow], size)
            if is_not_cycle(nums, forward, slow):
                break
            
            fast = next_step(fast, nums[fast], size)
            if is_not_cycle(nums, forward, fast):
                break
            
            fast = next_step(fast, nums[fast], size)
            if is_not_cycle(nums, forward, fast):
                break
            
            if slow == fast:
                return True            
            
    return False

def next_step(pointer, num_steps, size):
    result = (pointer+num_steps) % size
    if result < 0:
        result += size
        
    return result

def is_not_cycle(nums, previous_direction, pointer):
    current_direction = nums[pointer] >= 0
    if (current_direction != previous_direction) or (abs(nums[pointer] % len(nums)) == 0):
        return True
    return False