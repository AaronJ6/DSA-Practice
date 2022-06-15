from typing import List


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def isPalindrome( head):
    if not head:
        return True
    dummy = None 
    slow, fast = head, head
    prev = dummy
    while fast and fast.next:
        fast = fast.next.next
        nxt = slow.next
        slow.next = prev
        prev = slow
        slow = nxt
    
    # if we want to restore the original linkedlist, in case the func belongs to a big program
    # (did not implement in this script!)
    
    first = prev
    second = slow if not fast else slow.next
    while first and second:
        if first.val != second.val:
            return False
        first = first.next
        second = second.next

ob1 = ListNode(1)
ob2 = ListNode(2)
ob3 = ListNode(2)
ob4 = ListNode(1)

ob1.next = ob2
ob2.next = ob3
ob3.next = ob4

isPalindrome(ob1)