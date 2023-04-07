def zipper_lists(head_1, head_2):
    tracker = head_1
    current_1 = head_1.next
    current_2 = head_2
    count = 0
    
    while current_1 is not None and current_2 is not None:
        if count % 2 == 0:
            tracker.next = current_2
            current_2 = current_2.next
        else:
            tracker.next = current_1
            current_1 = current_1.next

        tracker = tracker.next
        count += 1

    if current_1 is not None:
        tracker.next = current_1
    if current_2 is not None:
        tracker.next = current_2

    return head_1

"""
Iterative approach:
n = length of list 1
m = length of list 2
Time: O(min(n, m))
Space: O(1)

"""