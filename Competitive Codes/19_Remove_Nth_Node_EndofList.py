
class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # calculate the length of the list
        cntr = 0
        cur = head
        while cur:
            cntr += 1
            cur = cur.next

        cur = head
        # special cases
        if cntr - n - 1 < 0:
            head = cur.next
            return head

        # get the index and delete it
        for i in range(cntr - n - 1):
            cur = cur.next
        cur.next = cur.next.next
        return head


# solution II - use 2 pointers
# define a left and right pointer, always keep their distance to be n
# when the right gets to the end , left is essentially at the nodel previous to what we want to remove
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left, right = head, head

        # move right pointer n times to the right
        for i in range(n):
            if right.next:
                right = right.next

            # if n = length of list --> remove the first element (e.g. length = 2 and n= 2, means removig first element)
            else:
                head = head.next
                return head

        # move pointers 1 step at a time, until right gets to the end of the list
        while right.next:
            left = left.next
            right = right.next
        # delete the node next of left
        if left.next:
            left.next = left.next.next
        return head