def sum_list(head):
    sum = 0
    while head is not None:
        sum += head.val
        head = head.next

    return sum

