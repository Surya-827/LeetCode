'''WAY 1'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# class Solution(object):
#     def removeElements(self, head:ListNode, val:int) ->ListNode:
#     """
#     :type head: ListNode
#     :type val: int
#     :rtype: ListNode
#     """
#         if head == None:
#             return head
#         elif head != None and head.next == None:
#             if head.val == val:
#                 return None
#             else:
#                 return head
#         else:
#             dummy = ListNode(0)
#             dummy.next = head
#             prev = dummy
#             while head != None:
#                 if head.val == val:
#                     prev.next = head.next
#                     head = prev
#                     prev = head
#                     head = head.next
#         return dummy.next



'''WAY 2'''

class Node(object):
    def __init__(self, data, nextNode):
        self.data = data
        self.nextNode = nextNode
    def setNext(self, n): self.nextNode = n
    def setData(self, d): self.data = d
    def getData(self): return self.data
    def getNext(self): return self.nextNode


class Linkedlist(object):

    def __init__(self, head=None):
        self.root = head
        self.size = 0

    def add(self, val):
        new_node = Node(val, self.root)
        self.root = new_node
        self.size += 1

    def size(self):
        return self.size

    def remove(self, data):
        currNode = self.root
        prevNode = None
        while currNode:
            if currNode.getData() == data:
                if prevNode:
                    prevNode.setNext(currNode.getNext())
                else:
                    self.root = currNode.getNext()
                self.size -= 1
                return True
            else:
                prevNode = currNode
                currNode = currNode.getNext()
        return False

    def show(self):
        ans = ""
        ptr = self.root

        while ptr:
            ans += str(ptr.data) + ","
            ptr = ptr.nextNode
        ans = ans.strip(",")

        if (len(ans)):
            return f"[{ans}]"
        else:
            return "[]"


if __name__ == "__main__":
    # head = [1,2,6,3,4,5,6],
    val = 6
    obj = Linkedlist()
    obj.add(1)
    obj.add(2)
    obj.add(6)
    obj.add(3)
    obj.add(4)
    obj.add(5)
    obj.add(6)
    obj.remove(6)

    while str(val) in list(obj.show())[1:-1]:
        obj.remove(val)
    print(obj.show())



"""
class Solution(object):
    def removeElements(self, head, val):
        if head is None:
            return
        # set a pointer to the head of the list
        curNode = head
        # and set a pointer to the previous node
        prevNode = None
        i = 0
        
        while curNode is not None:
            # if the head is the one removed
            if curNode.val == val and i == 0:
                head = curNode.next
                curNode = curNode.next
                continue # keep going if the head still needs to be changed
                # like in example [7,7,7,7] 7
            else:
                i+=1
            # else in the middle or end
            if curNode.val == val:
                prevNode.next = curNode.next
                curNode = prevNode.next
                continue
            
            prevNode = curNode
            curNode = curNode.next
            
        return head

"""