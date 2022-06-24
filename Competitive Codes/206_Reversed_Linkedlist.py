from pyparsing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self,head:Optional[ListNode]) ->Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            NewHead = curr.next
            curr.next = prev
            prev = curr
            curr = NewHead
        return prev


