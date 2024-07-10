def longest_streak(head):
    if head is None:
        return 0
        
    if head.next is None:
        return 1
        
    comparison_val = head.val
    curr_streak = 1
    max_streak = 0
    current = head.next
    while current:
        if current.val == comparison_val:
            curr_streak += 1
        else:
            if curr_streak > max_streak:
                max_streak = curr_streak
                comparison_val = current.val
                curr_streak = 1
        
        current = current.next
    return max_streak