# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        lst1 = head
        lst2 = head.next

        ref = None

        while head:
            ref = head.next
            head.next = head.next.next if head.next else None
            head = ref

        tmp = lst1

        while tmp.next:
            tmp = tmp.next

        tmp.next = lst2

        return lst1