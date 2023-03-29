def linked_list_find(head, target):
    if head is None:
        return False
    if head.val == target:
        return True
    return linked_list_find(head.next, target)

"""
Recursive approach
===================
n: number of nodes
Time: O(n)
Space: O(n)
"""