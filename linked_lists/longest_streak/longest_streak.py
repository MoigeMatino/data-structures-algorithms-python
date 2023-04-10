def longest_streak(head):
    prev = None
    max_streak = 0
    current_streak = 0
    current = head
    
    while current is not None:
        if current.val == prev:
            current_streak += 1
        else:
            current_streak = 1
        
        prev = current.val
        
        if current_streak > max_streak:
            max_streak = current_streak      
        
        current = current.next
    return max_streak