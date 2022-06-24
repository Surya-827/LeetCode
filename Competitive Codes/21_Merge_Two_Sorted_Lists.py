
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        if l1!=None and l2!=None:
            return None
        elif(l1!=None and l2==None):
            return l1
        elif(l2!=None and l1==None):
            return l2
        else:
            ptr = ListNode(0)
            p = ptr

            while l1!=None and l2!=None:
                if(l1.val<l2.val):
                    ptr.next = l1
                    l1 = l1.next
                else:
                    ptr.next = l2
                    l2 = l2.next
                p = p.next

            if l1!=None:
                p.next = l1
            if l2!=None:
                p.next = l2
            return ptr.next
