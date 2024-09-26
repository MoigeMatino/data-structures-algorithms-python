def palindrome(head):
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
    reversed_half_head = reverse_list(slow)
    is_identical = compare_halfs(head, reversed_half_head)
    
    # return linked list in the original order
    if is_identical:
        return True
    return False
    
    
def reverse_list(head):
    prev = None
    current = head
    
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
        
    return prev

def compare_halfs(head1, head2):
    while head1 and head2:
        if head1.val != head2.val:
            return False
        head1 = head1.next
        head2 = head2.next
    return True

