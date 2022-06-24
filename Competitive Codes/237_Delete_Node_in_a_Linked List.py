
class Node(object):
    def __init__(self,d,n):
        self.data = d
        self.next = n

    def setData(self,data):
        self.data = data

    def setNext(self,nextNode):
        self.next = nextNode

    def getData(self):return self.data

    def getNext(self):return self.next


class Linkedlist(object):

    def __init__(self,root=None):
        self.root = root
        self.size = 0

    def getSize(self): return self.size

    def addNode(self,val):
        new_node = Node(self.root,val)
        self.root = new_node
        self.size+=1

    def removeNode(self,val):
        prev = None
        curr_node = self.root

        while curr_node:
            if curr_node.getData()==val:
                if prev:
                    prev.setNext(curr_node.getNext())
                else:
                    self.root = curr_node.getNext()
                self.size-=1
            else:
                prev = curr_node
                curr_node = curr_node.getNext()


# Definition for singly-linked list.
# class ListNode(object):
# def __init__(self, x):
# self.val = x
# self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-plac

        e instead.
        """
        if node == None:
            pass
        else:
            next_node = node.next
            node.val = next_node.val
            node.next = next_node.next