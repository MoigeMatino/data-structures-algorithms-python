def reverse_list(head, prev=None):
    if head is None:
        return prev
    next = head.next
    head.next = prev
    return reverse_list(next, head)

"""
Recursive approach
n: number of nodes
Time: O(n)
Space: O(n)
"""
