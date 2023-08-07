class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def merge_lists(head_1, head_2):
    if head_1 is None and head_2 is None:
        return None
    if head_1 is None:
        return head_2
    if head_2 is None:
        return head_1
    if head_1.val < head_2.val:
        next_1 = head_1.next
        head_1.next = merge_lists(next_1, head_2)
        return head_1
    else: 
        next_2 = head_2.next
        head_2 = merge_lists(head_1, next_2)
        return head_2

"""
n = length of list 1
m = length of list 2
Time: O(min(n, m))
Space: O(min(n,m))

"""
