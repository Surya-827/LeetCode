class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

class Solution(object):

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head.next:
            return True

        slow,fast = head,head
        head2 = None

        while fast and fast.next:
            fast = fast.next.next
            head2,slow,head2.next = slow,slow.next,head2

        if fast:
            slow=slow.next

        while head2:
            if slow.val!=head2.val:
                return False
            head2 = head2.next
            slow=slow.next
        return True