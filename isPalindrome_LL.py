def isPalindrome(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    if not head:
        return None
    slow, fast = head, head
    prev = None
    
    while fast and fast.next: #*we are inverting all pointers to the other direction(taken care of by slow)
                              #*and the rest of the nodes are left alone, we make sure we reach only till half by the fast pointer
        fast = fast.next.next
        nxt = slow.next
        slow.next = prev
        prev = slow
        slow = nxt
    
    first = prev
    second = slow if not fast else slow.next #!we check if fast has reached the end or not to decide if we take 
                                            #! slow as the starting for second half not sure why else part
    
    while first and second:
        if first.val != second.val:
            return False
        first = first.next
        second = second.next
    
    return True