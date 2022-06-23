# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorderList(head):
    """
    :type head: ListNode
    :rtype: None Do not return anything, modify head in-place instead.
    """
    if not head:
        return None
    fast = head.next
    slow = head   
    
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    
    second = slow.next
    prev = slow.next = None
    while second:
        nxt = second.next
        second.next = prev
        prev = second
        second = nxt
        
    right = prev
    left = head
    
    while right:
        l_nxt, r_nxt = left.next, right.next
        left.next = right
        right.next = l_nxt
        right = r_nxt
        left = l_nxt