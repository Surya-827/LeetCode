
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return False
        else:
            fast = head
            slow = head
            while fast != None and fast.next != None:
                slow = slow.next
                fast = fast.next.next
                if fast == slow:
                    break
            if fast == None or fast.next == None:
                return False
            elif fast == slow:
                return True
            return False


# if __name__=="__main__":
#
#     s = Solution()
#     head = [3,2,0,-4]
#     pos=1
#     print(s.hasCycle(head))