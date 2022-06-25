class ListNode:
    def __init__(self,x):
        self.val=x
        self.next = None

class Solution(object):
    def detectCycle(self,head:ListNode):
        if head==None:
            return None
        else:
            fast = head
            slow = head
            cycle= False

            while fast!=None and fast.next!=None:
                slow = slow.next
                fast = fast.next.next

                if slow==fast:
                    cycle = True
                    break
            if(cycle==False):
                return None
            slow = head

            while slow!=fast:
                slow=slow.next
                fast=fast.next
            return slow