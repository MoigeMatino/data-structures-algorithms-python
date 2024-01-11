def longest_streak(head):
    current = head
    curr_val = head.val
    max_streak = 0
    curr_streak = 0
    
    while current:
        if current.val == curr_val:
            curr_streak += 1
        else:
            curr_val = current.val
            curr_streak = 1
            
        if curr_streak > max_streak:
                max_streak = curr_streak
        current = current.next  
    return max_streak

"""

n = number of nodes
Time complexity: O(n)
Space Complexity: O(1)


"""