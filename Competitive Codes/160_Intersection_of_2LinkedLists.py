# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Hash Set Solution
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a = headA
        b = headB
        aSet = set()
        # create a set of all A elements
        while a:
            aSet.add(a)
            a = a.next
        # go over b elements and compare to A to see if exists , report teh first one that exists    
        while b:
            if b in aSet:
                return b
            b = b.next
        # if there is no interesection report null
        return


# Solution  II

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        cntrA = 0
        cntrB = 0
        a = headA
        b = headB
        # calculate length A
        while a:
            cntrA += 1
            a = a.next
        # calculate length A    
        while b:
            cntrB += 1
            b = b.next

        # calculate length difference  
        diff = abs(cntrA - cntrB)

        # increment the longer list to start at the same distance from intersection
        if cntrA < cntrB:
            for i in range(diff):
                headB = headB.next
        else:
            for i in range(diff):
                headA = headA.next

        # start at the same distance from intersection and compare the list elements         
        a = headA
        b = headB
        while a:
            if a == b:
                return a
            a = a.next
            b = b.next
        return

    # Solution III - O (m+n)


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a, b = headA, headB
        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a