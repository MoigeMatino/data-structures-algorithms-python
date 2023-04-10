def is_univalue_list(head):
    head_val = head.val
    current = head.next
    while current is not None:
        if current.val != head_val:
            return False
        current = current.next
        
    return True