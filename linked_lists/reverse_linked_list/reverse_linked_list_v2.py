def reverse_list(head, prev=None):
    if head is None:
        return None
    next = head.next
    head.next = prev
    return reverse_list(next, head)