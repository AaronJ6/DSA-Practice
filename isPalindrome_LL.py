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
    second = slow if not fast else slow.next #!we check fast if its an even no. of list or not
                                            #!testcase for "else" => [1,0,1]
    
    while first and second:
        if first.val != second.val:
            return False
        first = first.next
        second = second.next
    
    return True