class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def merge_lists(head_1, head_2):
    dummy_head = Node(None)
    tracker = dummy_head
    while head_1 is not None and head_2 is not None:
        if head_1.val < head_2.val:
            tracker.next = head_1
            head_1 = head_1.next
        else:
            tracker.next = head_2
            head_2 = head_2.next
        
        tracker = tracker.next
    
    if head_1 is not None:
        tracker.next = head_1
    if head_2 is not None:
        tracker.next = head_2

    return dummy_head.next

"""
Iterative approach
n = length of list 1
m = length of list 2
Time: O(min(n, m))
Space: O(1)

"""
