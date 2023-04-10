def is_univalue_list(head, prev_val = None):
    if head is None:
        return True
    if prev_val is None or head.val == prev_val:
        return is_univalue_list(head.next, head.val)
    else:
        return False