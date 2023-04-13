def remove_node(head, target_val):
    if head is None:
        return None

    if head.val == target_val:
        return head.next

    head.next = remove_node(head.next, target_val)
    return head

"""
Recursive approach
n -  number of nodes
Time: O(n)
Space: O(n)

"""