def longest_streak(head):
    if head is None:
        return 0
    
    max_streak = 0
    current_streak = 1
    comparison_val = head.val
    current = head.next
    
    while current is not None:
        if current.val == comparison_val:
            current_streak += 1
        else:
            current_streak = 1
            comparison_val = current.val
        
        
        if current_streak > max_streak:
            max_streak = current_streak      
        
        current = current.next
    return max(max_streak, current_streak)