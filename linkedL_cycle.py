def hasCycle(head): #!Simple fast and slow pointer
    """
    :type head: ListNode
    :rtype: bool
    """
    
    curr, skip = head, head
    
    while(skip and skip.next):
        curr = curr.next
        skip = skip.next.next
        if curr == skip:
            return True
    return False

"""     if head: #!USING HASHSET
    hash = []
    curr = head
    hash.append(curr)
    curr = curr.next
    while curr:
        if curr in hash:
            return True
        hash.append(curr)
        curr = curr.next
    return False """

