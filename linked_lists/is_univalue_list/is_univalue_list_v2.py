def is_univalue_list(head):
    if head.next is None:
        return True
    next = head.next
    if head.val != next.val:
        return False
    
    return is_univalue_list(next)