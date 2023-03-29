def sum_list(head):
    if head is None:
        return 0
    return head.val + sum_list(head.next)

"""
n: number of nodes in linked list
Time: O(n)
Space: O(n); this is because of the memory 
"""
