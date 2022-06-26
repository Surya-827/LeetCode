
class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

# WAY 1
class Solution:
    def deleteDuplicates(self,head:Optional[ListNode]) -> ListNode:

        if not head:return None

        flag = True
        result_head = ListNode(0)
        result_tail = result_head
        ptr = head
        nextPtr = ptr.next

        while ptr:
            if nextPtr is None:
                if flag:
                    result_tail.next = ListNode(ptr.val)
                break
            else:
                if nextPtr.val!=ptr.val:
                    if flag:
                        result_tail.next = ListNode(ptr.val)
                        result_tail = result_tail.next
                    else:
                        flag = True
                else:
                    flag = False
                ptr = ptr.next
                nextPtr = nextPtr.next
        return result_head.next


# WAY 2
def deleteDuplicates(self,head):

    if not head:return None
    if head==None:return head

    else:
        d = dict()
        curr = head

        while curr!=None:
            if curr.val in d:
                d[curr.val]+=1
            else:
                d[curr.val]=1
            curr = curr.next

        values = []
        curr = head
        while curr!=None:
            if d[curr.val]>1:
                pass
            else:
                values.append(curr.val)
            curr = curr.next

        if values==[]:
            return None
        else:
            node1 =ListNode(values[0])
            head = node1
            for entries in values[1:]:
                new_node = ListNode(entries)
                node1.next = new_node
                node1 = new_node
            return head




