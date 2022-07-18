# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        left = head
        right = self.getMiddle(head)
        temp = right.next
        right.next = None
        right = temp
        left = self.sortList(left)
        right = self.sortList(right)
        return self.merge(left, right)
    def getMiddle(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    def merge(self, left, right):
        temp = temp2 = ListNode()
        while left and right:
            if left.val < right.val:
                temp2.next = left
                left = left.next
            else:
                temp2.next = right
                right = right.next
            temp2 = temp2.next
        if left:
            temp2.next = left
        if right:
            temp2.next = right
        return temp.next