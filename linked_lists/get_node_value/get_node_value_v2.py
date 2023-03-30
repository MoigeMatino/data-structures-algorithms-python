def get_node_value(head, index):
    if head is None:
        return None
    if index == 0:
        return head.val
    
    return get_node_value(head.next, index-1)

"""
Recursive approach
====================
n: number of nodes
Time: O(n)
Space: O(n)
"""