# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head, n): #!NEETCODE
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    if not head:
        return None
    dummy = ListNode(0,head)
    left = dummy
    right = head
    
    while n>0 and right:
        right = right.next
        n-=1
        
    while right:
        left = left.next
        right = right.next

    left.next = left.next.next
    return dummy.next

""" def removeNthFromEnd(head, n): #!MY CODE
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
 """