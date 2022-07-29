class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        prev = dummy
        node = head
        while node:
            curr = self.reverse(prev, node, k)
            prev = node
            node = curr.next

        return dummy.next

    def reverse(self, prev: ListNode, curr: ListNode, k: int) -> ListNode:
        '''
        Reverses the next k-group in place and returns the last node we visited.
        This allows the caller to resume linked list traversal from last visited.
        '''
        # checks if there are enough elements to reverse
        p = None
        node = curr
        for i in range(k):
            if not node:
                # returns the last node
                return p
            p = node
            node = node.next

        # starting at current node, reverse linkedlist in place
        p = None
        node = curr
        while node and k:
            tmp = node.next
            node.next = p
            p = node
            node = tmp
            k -= 1

        # link prev to start of k-group
        prev.next = p
        # link end of k-group to remaining nodes
        curr.next = node

        # returns the end of k-group
        return curr