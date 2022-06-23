def removeNthFromEnd(head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    if not head:
        return None
    temp = head
    size = 0
    while temp:
        size+=1
        temp = temp.next
    if size == 1:
        return None
    
    i = 1
    chk = size-n
    temp = head
    if chk == 0:
        head = temp.next
        return head
    while temp:
        if i==chk:
            temp.next = temp.next.next
            return head
        temp = temp.next
        i+=1