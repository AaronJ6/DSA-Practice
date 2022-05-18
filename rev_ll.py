def reverseList(head): #!RECURSIVE NEETCODE
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if not head:
        return None
    
    newHead = head
    if head.next:
        newHead = reverseList(head.next)
        head.next.next = head
    head.next = None
    
    return newHead


""" ListNode* reverseList(ListNode* head) { #!Used C++ and with 3 pointers
    ListNode* temp = NULL;
    temp = head;
    ListNode* next = NULL;
    ListNode* rev = NULL;
    while(temp != NULL)
    {
        next = temp->next;
        temp->next = rev;
        rev = temp;
        temp = next;
    }
    head = rev;
    return(head);        
}
 """