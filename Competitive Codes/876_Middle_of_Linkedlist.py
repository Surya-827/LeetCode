class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow_ptr, fast_ptr = head, head

        while fast_ptr != None and fast_ptr.next != None:
            slow_ptr = slow_ptr.next

            fast_ptr = fast_ptr.next.next

        return slow_ptr