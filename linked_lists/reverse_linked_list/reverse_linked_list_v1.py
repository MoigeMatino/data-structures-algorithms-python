def reverse_list(head):
    previous = None
    current = head
    while current is not None:
        next = current.next
        current.next = previous
        previous = current
        current = next
    return previous.val

"""
Iterative approach
n - number of nodes
Time: O(n)
Space: O(1)
"""