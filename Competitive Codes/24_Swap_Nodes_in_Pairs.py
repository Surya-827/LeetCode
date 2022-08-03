# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head):
        cur, res = head, []

        while cur:
            res.append(cur.val)
            cur = cur.next

        ans1, ans2 = [j for i, j in enumerate(res) if i % 2 == 0], [j for i, j in enumerate(res) if i % 2 == 1]

        ans, min_len = [], min(len(ans1), len(ans2))

        for i in range(min_len):
            ans += [ans2[i]] + [ans1[i]]

        ans += ans2[min_len:] + ans1[min_len:]

        r1 = r2 = ListNode()

        for i in ans:
            r1.next = ListNode(i)
            r1 = r1.next

        return r2.next