def remove_nth_last_node(head, n):
    right = head
    left = head

    for _ in range(n):
        right = right.next

    while right.next is not None:
        right = right.next
        left = left.next
    left.next = left.next.next

    return head