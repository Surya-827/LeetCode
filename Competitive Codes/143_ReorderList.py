class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        def rev(node: ListNode, prev: ListNode) -> ListNode:
            if node == None:
                return prev

            next = node.next
            node.next = prev
            prev = node
            return rev(next, node)

        if head == None:
            return
        slow = head
        fast = head.next

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        secondsPosNode = slow.next
        slow.next = None
        secondsPosNode = rev(secondsPosNode, None)

        res = head
        prev = None

        while head != None and secondsPosNode != None:

            firNext = head.next
            secondNext = secondsPosNode.next

            if head != None:
                head.next = None
            if secondsPosNode != None:
                secondsPosNode.next = None

            if prev == None:
                prev = head
            else:
                prev.next = head

            head.next = secondsPosNode

            prev = secondsPosNode
            head = firNext
            secondsPosNode = secondNext

            if head != None:
                prev.next = head

        return res